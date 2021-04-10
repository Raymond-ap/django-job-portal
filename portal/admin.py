from django.contrib import admin
from .models import *


class JobRequirementInline(admin.TabularInline):
    model = JobRequirement
    extra = 3


class JobAdmin(admin.ModelAdmin):
    inlines = [JobRequirementInline]
    list_display = ('company_name', 'job_title', 'company_email',
                    'location', 'created', 'featured', 'approved')
    search_fields = ('company_name', 'job_title',
                     'company_email', 'company_email')


admin.site.register(Job, JobAdmin)


# ========= Category =============
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'created')
    search_fields = ('category',)
