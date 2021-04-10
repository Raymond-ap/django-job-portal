from django.shortcuts import render
from .models import Job


def loginPage(request):
    return render(request, 'portal/login.html')


def signup(request):
    return render(request, 'portal/register.html')


def homePage(request):
    jobs = Job.objects.filter(approved=True).order_by('-created')
    context = {
        'jobs': jobs
    }
    return render(request, 'portal/index.html', context)


def jobs(request):
    return render(request, 'portal/search.html')


# Job Detail View
def jobDetail(request, slug):
    job = Job.objects.filter(slug=slug)

    # try:
    #     job = Job.objects.filter(approved=True, slug=slug)
    # except Exception:
    #     pass

    context = {
        'job': job,
    }
    return render(request, 'portal/single.html', context)


def blog(request):
    return render(request, 'portal/blog-home.html')


def contact(request):
    return render(request, 'portal/contact.html')


def about(request):
    return render(request, 'portal/about-us.html')
