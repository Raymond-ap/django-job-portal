from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="home"),
    path('about', about, name="about"),
    path('jobs', jobs, name="jobs"),
    path('blog', blog, name="blog"),
    path('contact', contact, name="contact"),
    path('login', loginPage, name="login"),
    path('signup', signup, name="signup"),

    path('detail/<slug:slug>', jobDetail, name='detail'),
]
