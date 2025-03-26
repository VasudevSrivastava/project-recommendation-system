from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill, Domain
from django.core.exceptions import ValidationError


from django.core.exceptions import ValidationError

class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    skill = models.ManyToManyField(Skill)
    domain = models.ManyToManyField(Domain) # we may need to implement domain constraint at model level
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    github_link = models.URLField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="ratings")
    rating = models.IntegerField(null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1, rating__lte=5), name="valid_rating_range")
        ] 

class SavedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','project')


