from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'neptwit_blog/home.html', context)


def about(request):
    return render(request, 'neptwit_blog/about.html', {'title': 'About'})



