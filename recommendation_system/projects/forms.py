from .models import Project, Rating, ProjectComment
from django.forms import ModelForm
from django import forms
from skills.models import Skill

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "domain", "description", "skill", "github_link"]

    def clean_domain(self):
        domains = self.cleaned_data.get("domain", [])
        if not (1 <= len(domains) <= 3):
            raise forms.ValidationError("You must select between 1 and 3 domains.")
        return domains


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]

