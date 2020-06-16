from django.urls import path
from .views import PostListView, PostDetailView
from . import views


# Name arg is given on the path to differentiate from other app which have similar names
urlpatterns = [
    path('', PostListView.as_view(), name='neptwitblog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='neptwitblog-about'),
]
