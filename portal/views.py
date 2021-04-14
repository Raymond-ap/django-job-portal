from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.forms import inlineformset_factory
from django.http import HttpResponse

from .forms import *
from .filters import JobFilter
from .models import *


def loginPage(request):
    # AUTHENTICATE USER LOGIN
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect('jobs')
        else:
            messages.info(request, 'Invalid credentials')
    return render(request, 'portal/login.html')


def logoutFn(request):
    logout(request)
    return redirect('jobs')


def signup(request):
    # AUTHENTICATE USER SIGNUP
    if request.method == 'POST':
        data = request.POST

        if data['password'] == data['password2']:
            if User.objects.filter(username=data['username']).exists():
                messages.info(request, "Username already taken")
                return redirect('signup')
            elif User.objects.filter(email=data['email']).exists():
                messages.info(request, "email already taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=data['username'],
                    first_name=data['fname'],
                    last_name=data['lname'],
                    email=data['email'],
                    password=data['password']
                )
                user.save()
                login(request, user)
                return redirect('jobs')
        else:
            messages.error(request, 'Password does not match')

    return render(request, 'portal/register.html')


def homePage(request):
    filters = JobFilter(
        request.GET, queryset=Job.objects.filter(approved=True))
    result_filters = filters.qs

    context = {
        'filters': filters
    }
    if request.method == "GET" and 'search' in request.GET:
        return redirect('jobs')
    else:
        return render(request, 'portal/index.html', context)


def jobs(request):

    # PAGINATOR
    paginator = Paginator(Job.objects.filter(approved=True), 10)
    page_number = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_number)

    # FILTER JOB BY CATEGORY
    category = request.GET.get('category')
    if category == None:
        jobs = Job.objects.filter(approved=True).order_by('-created')
    else:
        jobs = Job.objects.filter(
            approved=True, category__category=category)

    # SEARCH FIELDS
    filters = JobFilter(
        request.GET, queryset=Job.objects.filter(approved=True))
    if jobs:
        page_objects = jobs
    else:
        page_objects = filters.qs

    context = {
        'jobs': jobs,
        'filters': filters,
        'page_objects': page_objects,
        'paginator': paginator
    }
    return render(request, 'portal/search.html', context)


# Job Detail View
def jobDetail(request, slug):

    try:
        job = Job.objects.get(approved=True, slug=slug)
        requirements = job.requirements.all()
    except Exception:
        return HttpResponse('Sorry this job does not exit\n<a href="/jobs">Return to home page</a>')

    context = {
        'job': job,
        'requirements': requirements,
    }
    return render(request, 'portal/single.html', context)


@login_required(login_url='login')
def addJob(request):
    jobFormSet = inlineformset_factory(
        Job, JobRequirement, fields=('requirement',), can_delete=True)

    formSet = jobFormSet()
    form = JobForm()

    if request.method == 'POST':
        data = request.POST

        formSet = jobFormSet()
        form = JobForm(request.POST)

        if form.is_valid():
            job_instance = form.save(commit=False)
            job_instance.job_title = data['job_title']
            job_instance.save()
            job = Job.objects.get(pk=job_instance.id)
            formSet = jobFormSet(request.POST, instance=job)
            if formSet.is_valid():
                formSet.save()
                return redirect('jobs')

    return render(request, 'portal/jpost_job.html',
                  {
                      'formSet': formSet,
                      'form': form,
                  })


def contact(request):
    if request.method == 'POST':
        data = request.POST
        form = Contact(name=data['name'], email=data['email'],
                       subject=data['subject'], message=data['message'])
        if not Contact.objects.filter(name=data['name'], email=data['email'], subject=data['subject'], message=data['message']).exists():
            form.save()
            messages.info(request, 'We will soon get back to you!!!')
            return redirect('contact')
    return render(request, 'portal/contact.html')


def about(request):
    return render(request, 'portal/about-us.html')
