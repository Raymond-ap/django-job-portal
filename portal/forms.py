from django import forms
from .models import *
from django.forms import ModelForm, inlineformset_factory


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', 'created', 'featured', 'approved')


class JobRequirementForm(forms.ModelForm):
    class Meta:
        model = JobRequirement
        fields = '__all__'
        exclude = ()


JobRequirementFormset = inlineformset_factory(
    Job, JobRequirement, form=JobRequirementForm, extra=3)
