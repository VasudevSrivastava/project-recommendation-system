from django.contrib import admin
from .models import Post, PostComment, Tag


admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Tag)
