from django.shortcuts import render
from portal.models import Category, Job
from rest_framework import generics, mixins
from .serializers import JobSerializer


class JobAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def get(self, request):
        return list(request)
