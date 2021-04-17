from django.urls import path
from .views import *

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Job Finder API",
        default_version='v1',
        description="API for job portal",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api', APIOverview, name="overview"),
    path('api/api-list', JobAPILIST.as_view()),
    path('api/job-update/<int:id>', JobUpdateView.as_view()),
    path('api/job-destroy/<int:id>', JobDestroy.as_view()),

    path('api/swagger/', schema_view.with_ui('swagger',
                                             cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
