from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'published', 'created')
    search_fields = ('title', 'category')


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'approved', 'created')
    search_fields = ('post', 'name','email')
