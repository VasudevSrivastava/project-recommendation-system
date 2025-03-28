from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.models import User
from django.db.models import Count, Sum, Avg
from django.core.paginator import Paginator



def home(request):
    project_scores = User.objects.annotate(stars=Sum('ratings__rating')).order_by('-stars')
    discussion_scores = User.objects.annotate(upvotes=Sum('comments__helpful_votes')).order_by('-upvotes')

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
    
