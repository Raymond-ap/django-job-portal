from django.shortcuts import render
from .models import *
from .filters import BlogFilter


def blog(request):
    blogs = Blog.objects.filter(published=True).order_by('-created')
    filters = BlogFilter(request.GET, queryset=blogs)
    blogs = filters.qs

    context = {
        'blogs': blogs,
        'filters':filters
    }
    return render(request, 'portal/blog-home.html', context)
