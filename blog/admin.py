from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published', 'created')
    search_fields = ('title', 'category')
