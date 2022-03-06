
from django.urls import path

from website.models import *
from . import views
from django.contrib import admin
from django.urls import path,include




urlpatterns = [
    path ("", views.home, name= 'index'),
    
  
    

    
  
    
]

