from django.shortcuts import render


def homePage(request):
    return render(request, 'portal/index.html')
