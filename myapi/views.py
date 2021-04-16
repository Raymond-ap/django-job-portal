from django.shortcuts import render
from portal.models import Category, Job
from rest_framework import generics, mixins
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def APIOverview(request):
    api_navs = {
        'Read docs': 'api/redoc/',
        'Swagger api': 'api/swagger/',
        'API Job List': 'api/api-list',
        'API Job Update': 'api/job-update/<int:id>',
        'API Job Delete': 'api/job-destroy/<int:id>',
    }
    return Response(api_navs)


class JobAPILIST(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class JobUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    lookup_field = 'id'

    def put(self, request, id):
        return self.update(request, id)


class JobDestroy(generics.GenericAPIView, mixins.DestroyModelMixin):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    lookup_field = 'id'

    def delete(self, request, id):
        return self.destroy(request, id)
