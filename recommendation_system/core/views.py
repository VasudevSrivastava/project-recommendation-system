from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Tag, PostComment
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, Value
from django.db.models.functions import Coalesce



def home(request):
    project_scores = User.objects.annotate(stars=Coalesce(Sum('ratings__rating'),Value(0))).order_by('-stars')

    discussion_scores = User.objects.annotate(
    project_upvotes=Coalesce(Sum('project_comments__helpful_votes'), Value(0)),
    post_upvotes=Coalesce(Sum('post_comments__helpful_votes'), Value(0))
    ).annotate(
        upvotes=F('project_upvotes') + F('post_upvotes')
    ).order_by('-upvotes')

    # discussion_scores = User.objects.annotate(
    # upvotes=Coalesce(Sum('project_comments__helpful_votes',), Value(0))).order_by('-upvotes')
    



    project_paginator = Paginator(project_scores, 5)
    discussion_paginator = Paginator(discussion_scores, 5)

    project_page = request.GET.get("project_page")
    discussion_page = request.GET.get("discussion_page")

    project_users = project_paginator.get_page(project_page)
    discussion_users = discussion_paginator.get_page(discussion_page)


    context = {'project_scores':project_users,
               'discussion_scores':discussion_users,
               }
    
    return render(request,'core/home.html',context)
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post-list')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self,**kwargs):
        post = Post.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)

        #view increment logic
        if not post.user or post.user!= self.request.user:   
            post.views += 1
            post.save(update_fields=['views'])
            
        #comment logic
        comments = post.comments.select_related("user","parent").order_by("created_at")
        nested_comments = get_comment_tree(comments)

        
        context["nested_comments"] = nested_comments
        return context
    
class PostListView(ListView):
    model = Post
    #paginate_by = 10

    def get_queryset(self):
        posts = Post.objects.all()

        tag_filters = self.request.GET.getlist("tag_filters")
        
        if tag_filters:
            posts = posts.filter(tag__name__in=tag_filters)
       # print(posts)
        sort_by = self.request.GET.get("sort",'-created_at')
        posts = posts.order_by(sort_by)

        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        selected_tag_filters= self.request.GET.getlist("tag_filters")
        context["selected_tag_filters"] = selected_tag_filters

        context["tag"] = Tag.objects.all()
        return context


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        form.save_m2m() 
        return super().form_valid(form)
    


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'




@login_required
def add_comment(request,post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
            parent_id = request.POST.get('parent_id')
            content = request.POST.get('content')
            parent = get_object_or_404(PostComment, id=parent_id) if parent_id else None

            if content:
                PostComment.objects.create(user=request.user, post=post, content=content, parent=parent)

    return redirect('post-detail', pk=post_id)


@login_required
def upvote_comment(request, comment_id):
    comment = get_object_or_404(PostComment, id=comment_id)
    comment.vote_helpful()
    return redirect('post-detail', pk=comment.post.id)
    

def get_comment_tree(comments):
    comment_map = {comment.id : comment for comment in comments}
    tree = []

    for comment in comments:
        if comment.parent:
            parent = comment_map.get(comment.parent.id)
            if not hasattr(parent,"nested_replies"):
                parent.nested_replies = []
            parent.nested_replies.append(comment)
        else:
            tree.append(comment)

    return tree


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(PostComment, id=comment_id, user=request.user)

    if request.method == 'POST':
        comment.content = request.POST.get("content")
        comment.save()
        return redirect('post-detail',pk=comment.post.id)
    
    return render(request,'core/edit_comment.html',{"comment":comment})

@login_required
def delete_comment(request,comment_id):
    comment = get_object_or_404(PostComment,id=comment_id,user=request.user)
    post = comment.post    
    comment.delete()

    return redirect('post-detail',pk=post.id)
