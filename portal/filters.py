import django_filters
from .models import *
from django import forms


class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ('job_title', 'category', 'location')

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'widget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keyword...'})
                },
            },

        }
