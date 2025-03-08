from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project-list"), 
    path("add/", views.ProjectCreateView.as_view(), name="project-add"),
    path("<int:pk>/update/", views.ProjectUpdateView.as_view(), name="project-update"), 
    path("<int:pk>/delete/", views.ProjectDeleteView.as_view(), name="project-delete"),
    path("<int:pk>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("<int:project_id>/save", views.save_project, name="project-save"),
    path("<int:project_id>/unsave", views.unsave_project, name="project-unsave"),
]
