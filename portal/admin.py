from django.contrib import admin
from .models import *

#################### JOb Admin ####################


class JobRequirementInline(admin.TabularInline):
    model = JobRequirement
    extra = 7


class JobAdmin(admin.ModelAdmin):
    inlines = [JobRequirementInline]
    list_display = ('company_name', 'job_title', 'company_email',
                    'location', 'created', 'featured', 'approved')
    search_fields = ('company_name', 'job_title',
                     'company_email', 'company_email')


admin.site.register(Job, JobAdmin)


#################### Category ####################
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'created')
    search_fields = ('category',)


#################### Contact ####################
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date', 'viwed')
    search_fields = ('name', 'email', 'subject')


admin.site.register(JobRequirement)
