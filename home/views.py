from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("A view esta funcionado ")

def index(request):
    return render( request,'index.html')

