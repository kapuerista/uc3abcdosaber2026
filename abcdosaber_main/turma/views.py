from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def turma(request):
    return HttpResponse("<p>Olá, sou a view do app Turma!</p>")
