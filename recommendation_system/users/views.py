from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from projects.models import SavedProject, Project
from skills.models import Skill
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Your account has been created. You are now able to log in!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    saved_projects= SavedProject.objects.filter(user=request.user)
    user_projects = Project.objects.filter(user=request.user)
    context = {
        'saved_projects':saved_projects,
        'user_projects':user_projects,
    }
    return render(request, 'users/profile.html', context)
    

@login_required
def update_profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request," Profile updated sucessfully! ")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'users/update_profile.html', context)



def user_profile(request,username):
   # user = User.objects.get(username=username)
    user = get_object_or_404(User,username=username)
    user_projects = Project.objects.filter(user=user)
    context = {
        'user': user,
        'user_projects':user_projects,
    }
    return render(request, 'users/user_profile.html', context)