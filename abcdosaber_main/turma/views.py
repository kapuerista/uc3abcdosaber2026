from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from turma.models import Turma


def turma(request):
    return HttpResponse("<p>Olá, sou a view do app Turma!</p>")


def listar_turmas(request):
    lista_turmas = Turma.objects.all()

    contexto = {
        'turmas': lista_turmas
    }

    return render(request, 'turma/listarTurmas.html', contexto)


def cadastrar_turma(request):

    contexto = {
        'turmas': Turma.objects.all()
    }

    return render(request, 'turma/cadastroTurma.html', contexto)


def registro_ausencia(request):
    return render(request, 'turma/registroAusencia.html')


def carregar_ausencia_alunos(request):
    return render(request, 'turma/registroAusencia.html')


def pagina_em_construcao(request):
    return render(request, 'turma/paginaemconstrucao.html')


def excluir(request, id):
    turma = get_object_or_404(Turma, id=id)

    turma.delete()

    return redirect('turma:listar')