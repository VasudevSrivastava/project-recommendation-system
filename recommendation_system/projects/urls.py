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
    path("<int:project_id>/rate", views.rate_project, name="project-rate"),
    path("api/recommendations/", views.ProjectRecommendationView.as_view(), name="get-recommendations"),
    path("recommendations/", views.project_recommendation_view, name="recommendations"),
    path("comment/<int:project_id>/add", views.add_comment, name="project-add-comment"),
    path("comment/<int:comment_id>/upvote", views.upvote_comment, name="project-upvote-comment"),
    path("comment/<int:comment_id>/edit", views.edit_comment, name="project-edit-comment"),
    path("comment/<int:comment_id>/delete", views.delete_comment, name="project-delete-comment"),
    
]
