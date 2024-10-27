from django.contrib import admin
from django.urls import path
from Contact import views
from django.contrib.auth import views as auth_views
from . import *
from Contact.models import Contact


urlpatterns = [
    path("", views.contact , name="contact"),
    path("Contact/", views.Contacts, name="Contact"),
   
  
]