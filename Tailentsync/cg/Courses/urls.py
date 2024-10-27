from django.contrib import admin
from django.urls import path
from Courses import views
from django.contrib.auth import views as auth_views
from . import *


urlpatterns = [
    path("", views.Courses , name="Courses"),
    path("search", views.search_Courses , name="search_Courses"),
    
   
  
]