from django.shortcuts import render


def homePage(request):
    return render(request, 'portal/index.html')

# ====================


# ====================
def about(request):
    return render(request, 'portal/about-us.html')



def category(request):
    return render(request, 'portal/category.html')
