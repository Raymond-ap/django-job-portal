from portal.models import *
from django.db.models import Count
from blog.models import *


def Processors(request):
    jobs = Job.objects.filter(approved=True).order_by('-created')
    categories = Category.objects.all().order_by('id')
    blogs = Blog.objects.filter(published=True).order_by('-id')
    blog_count = blogs.count()

    return {
        'categories': categories,
        'jobs': jobs,
        'blog_count': blog_count,
        'blogs': blogs,
    }
