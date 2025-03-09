from .models import Project, Rating
from django.forms import ModelForm
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title","description","skill","github_link"]
        widgets = {
            "skill":forms.SelectMultiple(attrs={"class":"form-control"})
        }

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]
