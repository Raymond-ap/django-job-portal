from django.contrib import admin
from .models import *


class JobRequirementInline(admin.TabularInline):
    model = JobRequirement
    extra = 3


class JobAdmin(admin.ModelAdmin):
    inlines = [JobRequirementInline]

admin.site.register(JobAdmin, JobRequirementInline)