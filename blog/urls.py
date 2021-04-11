from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog', blog, name="blog"),
]
