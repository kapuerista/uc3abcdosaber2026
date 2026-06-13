from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listar_instrutores(request):
    return render(request, 'instrutor/ListarInstrutores.html')

def cadastrar_instrutor(request):
    return render(request, 'instrutor/cadastroInstrutor.html')
