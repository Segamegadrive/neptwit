from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # To allow current logged in user to post new twit. If this method isn't defined, throws an IntegrityError
    # Overriding form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # To allow current logged in user to post new twit. If this method isn't defined, throws an IntegrityError
    # Overriding form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'neptwit_blog/about.html', {'title': 'About'})



