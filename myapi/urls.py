from django.urls import path
from .views import *


urlpatterns = [
    path('api-overview', JobAPIView.as_view()),
]
