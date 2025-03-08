from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from .models import SavedProject
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required



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
        context = super().get_context_data(**kwargs)
        if len(SavedProject.objects.all().filter(user=self.request.user,project=Project.objects.all().get(id=self.kwargs['pk']))) == 0:
            context["is_saved"] = False
        else:
            context["is_saved"] = True
        return context
        

class ProjectListView(ListView):
    model = Project
    paginate_by = 10


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

