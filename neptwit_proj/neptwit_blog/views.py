from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'neptwit_blog/home.html')


def about(request):
    return render(request, 'neptwit_blog/about.html', {'title': 'About'})



