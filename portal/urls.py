from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="home"),
    path('about', about, name="about"),
    path('jobs', jobs, name="jobs"),
    path('contact', contact, name="contact"),
    path('login', loginPage, name="login"),
    path('signup', signup, name="signup"),
    path('logout', logoutFn, name="logout"),
    path('post', addJob, name="post"),
    path('account', account, name="account"),

    path('detail/<slug:slug>', jobDetail, name='detail'),
]
