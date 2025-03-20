from .models import Project, Rating
from django.forms import ModelForm
from django import forms
from skills.models import Skill

class ProjectForm(ModelForm):
    skill = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Not used directly but needed for validation
        required=True
    )
    class Meta:
        model = Project
        fields = ["title","description","skill","github_link"]
        # widgets = {
        #     "skill":forms.SelectMultiple(attrs={"class":"form-control"})
        # }

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]
