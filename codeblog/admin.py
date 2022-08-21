from django.contrib import admin

# Register your models here.

from .models import Genre, Post, Content 

admin.site.register(Genre)
admin.site.register(Post)
admin.site.register(Content)
