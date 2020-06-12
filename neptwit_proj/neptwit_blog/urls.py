from django.urls import path
from . import views


# Name arg is given on the path to differentiate from other app which have similar names
urlpatterns = [
    path('', views.index, name='neptwitblog-home')
]