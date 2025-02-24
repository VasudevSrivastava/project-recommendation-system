from django.db import models

from django.contrib.auth.models import User
from skills.models import Skill

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=100, blank = True)
    image = models.ImageField()
    skills = models.ManyToManyField(Skill)