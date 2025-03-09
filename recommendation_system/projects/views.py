from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Project, SavedProject, Rating 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg



class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project-list')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self,**kwargs):
        project = Project.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)

        #view increment logic
        if not project.user or project.user!= self.request.user:   
            project.views += 1
            project.save(update_fields=['views'])
        #rating fetch logic
        rating = Rating.objects.filter(project=project).aggregate(Avg("rating",default=0))
        user_rating = None
        if self.request.user.is_authenticated:
            rating_obj = Rating.objects.filter(user=self.request.user, project=project).first()
            if rating_obj:
                user_rating = rating_obj.rating
        context["user_rating"] = user_rating
        context["rating"] = round(rating.get("rating__avg"),2)
        context["is_saved"] = SavedProject.objects.filter(user=self.request.user,project=project).exists()
        return context
        

class ProjectListView(ListView):
    model = Project
    #paginate_by = 10

    def get_queryset(self):
        queryset = Project.objects.annotate(avg_rating=Avg("rating__rating"))
        return queryset



class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        form.save_m2m() 
        return super().form_valid(form)

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/'

@login_required
def save_project(request,project_id):
    saved_project,created = SavedProject.objects.get_or_create(user=request.user,project=Project.objects.all().get(id=project_id))
    if created:
        messages.success(request,"Project Saved Successfully")
    else:
        messages.info(request,"Project was already saved")
    return redirect(reverse('project-detail',kwargs={'pk':project_id}))

@login_required
def unsave_project(request,project_id):
    project = SavedProject.objects.get(user=request.user,project=Project.objects.all().get(id=project_id))
    project.delete()
    messages.warning(request,"Project Unsaved Successfully")
    return redirect(reverse('project-detail',kwargs={'pk':project_id}))


@login_required
def rate_project(request,project_id):
    rating_object,created = Rating.objects.get_or_create(user=request.user,project=Project.objects.get(id=project_id))
    rating_object.rating = request.POST['rating']
    rating_object.save(update_fields=['rating'])

    return redirect(reverse('project-detail',kwargs={'pk':project_id}))