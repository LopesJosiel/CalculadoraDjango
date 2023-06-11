from django.shortcuts import render
from django.http import HttpResponse
#criação de views aqui
def index (request):
    return HttpResponse ('o aplicativo foi iniciado com sucesso')
