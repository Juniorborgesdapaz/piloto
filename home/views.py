from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("A view está funcionando")

def home(request):
    return render(request, 'index.html')
