from django.shortcuts import render



def index(request):
    return render(request, 'mysite/index.html')

def contact(request):
    return render(request, 'mysite/page-contact.html')


def about(request):
    return render(request, 'mysite/about.html')

def sitemap(request):
    return render(request, 'mysite/page-sitemap.html')