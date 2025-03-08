from .models import Project
from django.forms import ModelForm
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title","description","skill","github_link"]
        widgets = {
            "skill":forms.SelectMultiple(attrs={"class":"form-control"})
        }