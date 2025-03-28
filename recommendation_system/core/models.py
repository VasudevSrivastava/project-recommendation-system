from django.db import models
from projects.models import ProjectComment
from django.contrib.auth.models import User



class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    tag = models.ForeignKey(Tag,null=True,blank=True, on_delete=models.SET_NULL, related_name='posts')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="posts")
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    votes = models.PositiveIntegerField(default=0)




class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, null=True,on_delete=models.SET_NULL, related_name='post_comments')
    parent = models.ForeignKey('self',null=True,blank=True, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    helpful_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Comment by {self.user} on {self.post.title}'
    
    def vote_helpful(self):
        self.helpful_votes += 1
        self.save()