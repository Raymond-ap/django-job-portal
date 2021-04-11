import django_filters
from django import forms
from .models import *


class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = ('title',)

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'widget': forms.TextInput(attrs={'class': '', 'placeholder': 'Search blog'})
                }
            }
        }
