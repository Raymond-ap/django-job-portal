from django.contrib import admin
from .models import *


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title',
                    'category', 'created', 'approved')
    search_fields = ('company_name', 'job_title', 'category')
