from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    
      # Associa a URL raiz do app com a view `index`
]
