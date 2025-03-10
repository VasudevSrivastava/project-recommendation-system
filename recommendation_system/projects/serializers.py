from rest_framework import serializers
from .models import Project, Rating

class ProjectSerializer(serializers.ModelSerializer):
    similarity_score = serializers.FloatField()
    rating = serializers.FloatField()
    skill_names = serializers.ListField()
    class Meta:
        model = Project
        fields = ['id','title','description','github_link','skill','similarity_score','rating','skill_names']
        