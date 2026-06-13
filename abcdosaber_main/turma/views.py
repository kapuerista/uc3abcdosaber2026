from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def turma(request):
    return HttpResponse("<p>Olá, sou a view do app Turma!</p>")

def listar_turmas(request):
    return render(request, 'listarTurmas.html')

def cadastrar_turma(request):
    return render(request, 'cadastroTurma.html')

def registro_ausencia(request):
    return render(request, 'registroAusencia.html')

def pagina_em_construcao(request):
    return render(request, 'paginaemconstrucao.html')