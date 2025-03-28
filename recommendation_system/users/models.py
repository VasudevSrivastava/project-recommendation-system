from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=100, blank = True)
    skills = models.ManyToManyField(Skill)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    linkedin_profile = models.URLField(null=True, blank=False)
    github_profile = models.URLField(null=True, blank=False)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height>300 or img.width>300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
        return f"{self.user}"