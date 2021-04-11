from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog', blog, name="blog"),
    path('blog_detail/<slug:slug>', blogDetail, name="blog_detail"),
]
