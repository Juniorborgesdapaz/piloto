from django.http import HttpResponse
from django.shortcuts import render

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request, 'contato.html')
