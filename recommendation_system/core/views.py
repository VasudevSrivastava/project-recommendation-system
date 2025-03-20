from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.models import User
from django.db.models import Count

def home(request):
    top_users = User.objects.annotate(contributions=Count('project')).order_by('-contributions')[:5]
    context = {'top_users':top_users}
    return render(request,'core/home.html',context)
    
