from .models import *
from django.db.models import Count


def Processors(request):
    jobs = Job.objects.filter(approved=True).order_by('-created')
    categories = Category.objects.all().order_by('-id')

    return {
        'categories': categories,
        'jobs':jobs
    }
