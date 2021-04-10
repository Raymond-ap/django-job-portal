from django.shortcuts import render
from .models import *
from .filters import JobFilter


def loginPage(request):
    return render(request, 'portal/login.html')


def signup(request):
    return render(request, 'portal/register.html')


def homePage(request):
    return render(request, 'portal/index.html')


def jobs(request):
    # Filter Jobs by category
    category = request.GET.get('category')
    if category == None:
        jobs = Job.objects.filter(approved=True).order_by('-created')
    else:
        jobs = Job.objects.filter(
            approved=True, category__category=category)

    filters = JobFilter(request.GET, queryset=Job.objects.filter(approved=True))
    jobs = filters.qs

    context = {
        'jobs': jobs,
        'filters': filters
    }
    return render(request, 'portal/search.html', context)


# Job Detail View
def jobDetail(request, slug):

    try:
        job = Job.objects.get(approved=True, slug=slug)
        requirements = job.requirements.all()
    except Exception:
        pass

    context = {
        'job': job,
        'requirements': requirements,
    }
    return render(request, 'portal/single.html', context)


def blog(request):
    return render(request, 'portal/blog-home.html')


def contact(request):
    return render(request, 'portal/contact.html')


def about(request):
    return render(request, 'portal/about-us.html')
