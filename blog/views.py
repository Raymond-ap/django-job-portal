from django.shortcuts import render, redirect
from .models import *
from .filters import BlogFilter
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import BlogCommentForm
from django.contrib import messages


def blog(request):
    blogs = Blog.objects.filter(published=True).order_by('-created')
    filters = BlogFilter(request.GET, queryset=blogs)
    blogs = filters.qs

    # PAGINATOR
    paginator = Paginator(blogs, 15)
    page_number = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_number)

    context = {
        'blogs': blogs,
        'filters': filters,
        'page_objects': page_objects
    }
    return render(request, 'portal/blog-home.html', context)


def blogDetail(request, slug):
    form = BlogCommentForm()

    try:
        blog = Blog.objects.get(slug=slug, published=True)
        comments = BlogComment.objects.filter(
            post=blog, approved=True).order_by('-id')
    except Exception:
        return HttpResponse('Sorry this blog does not exit\n<a href="/blog/blog">Return to home page</a>')

    # PROCESS COMMENT
    if request.method == 'POST':
        data = request.POST
        comment = BlogComment(
            post=blog, name=data['name'], email=data['email'], message=data['message'])
        if not BlogComment.objects.filter(post=blog, name=data['name'], email=data['email'], message=data['message']).exists():
            comment.save()
            return redirect('blog_detail', slug=slug)

    context = {
        'blog': blog,
        'comments': comments,
        'form': form
    }
    return render(request, 'portal/blog-single.html', context)
