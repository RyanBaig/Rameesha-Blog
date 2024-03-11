# I have crreated this file - Ryan
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="Home"),
    path('post/<int:id>', views.blogpost, name="BlogPost"),
    path('search/', views.search, name="Search"),
]
