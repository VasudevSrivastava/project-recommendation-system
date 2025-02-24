from django.contrib import admin

from .models import Project, SavedProject, Rating

admin.site.register(Project)
admin.site.register(SavedProject)
admin.site.register(Rating)
