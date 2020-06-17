from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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
    paginate_by = 5


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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # To allow current logged in user to post new twit. If this method isn't defined, throws an IntegrityError
    # Overriding form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Making sure update is allowed only for logged in user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # success_url to redirect to homepage
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'neptwit_blog/about.html', {'title': 'About'})



