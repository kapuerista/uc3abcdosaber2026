from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def utilitarios(request):
    return HttpResponse("<p>Olá, sou a view do app Utilitário!</p>")
