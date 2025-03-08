from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from django.urls import reverse_lazy


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project-list')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    model = Project
    paginate_by = 10


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        form.save_m2m()  # Save ManyToManyField separately
        return super().form_valid(form)



class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/'