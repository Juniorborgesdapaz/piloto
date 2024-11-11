from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # Para acessar a view de texto simples
    path('', views.home, name='home'),  # A view que renderiza index.html
]
