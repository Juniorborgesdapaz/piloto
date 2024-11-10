from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    
      # Associa a URL raiz do app com a view `index`
]
