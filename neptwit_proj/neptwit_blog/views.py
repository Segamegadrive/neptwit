from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.http import HttpResponse
from .models import Post


# function based views/controller
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'neptwit_blog/home.html', context)


# Class based view
class PostListView(ListView):
    model = Post
    template_name = 'neptwit_blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'neptwit_blog/about.html', {'title': 'About'})



