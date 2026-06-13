from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cadastrar_aluno(request):
    return render(request, 'aluno/cadastroAluno.html')

def listar_alunos(request):
    return render(request, 'aluno/listarAlunos.html')
