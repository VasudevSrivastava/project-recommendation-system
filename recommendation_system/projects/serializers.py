from rest_framework import serializers
from .models import Project, Rating

class ProjectSerializer(serializers.ModelSerializer):
    similarity_score = serializers.FloatField()

    class Meta:
        model = Project
        fields = ['id','title','description','github_link','similarity_score']