from django.shortcuts import render


def homePage(request):
    return render(request, 'portal/index.html')

# ====================


# ====================
def searchPage(request):
    return render(request, 'portal/search.html')


def loginPage(request):
    return render(request, 'portal/login.html')

def signup(request):
    return render(request, 'portal/register.html')

def category(request):
    return render(request, 'portal/category.html')


def blog(request):
    return render(request, 'portal/blog-home.html')


def contact(request):
    return render(request, 'portal/contact.html')


def about(request):
    return render(request, 'portal/about-us.html')

