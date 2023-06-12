from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfunctioncall (request):
    return HttpResponse ("Hello World")

def myfunctionabout (request):
    return HttpResponse ("Sobre o aplicativo da calculadora")

def calcpage (request):
    return render (request, 'index.html')