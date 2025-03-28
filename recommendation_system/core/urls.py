from django.urls import path
from . import views


urlpatterns = [
    path("",views.home, name='home'),
    path("about/",views.about, name='about'),
    path("posts/",views.PostListView.as_view(), name="post-list"),
    path("posts/add/", views.PostCreateView.as_view(), name="post-add"),
    path("posts/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"), 
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/comment/<int:post_id>/add", views.add_comment, name="add-comment"),
    path("posts/comment/<int:comment_id>/upvote", views.upvote_comment, name="upvote-comment"),
    path("posts/comment/<int:comment_id>/edit", views.edit_comment, name="edit-comment"),
    path("posts/comment/<int:comment_id>/delete", views.delete_comment, name="delete-comment"),
]