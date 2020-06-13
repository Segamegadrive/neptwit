from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Sagar',
        'title': 'Sagar title',
        'content': 'Sagar content',
        'date_posted': '13 June 2020'
    },
    {
        'author': 'Avana',
        'title': 'Avana title',
        'content': 'Avana content',
        'date_posted': '14 June 2020'
    }
]


def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'neptwit_blog/home.html', context)


def about(request):
    return render(request, 'neptwit_blog/about.html', {'title': 'About'})



