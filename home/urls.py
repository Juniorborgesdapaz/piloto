from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [  
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato') 
]
