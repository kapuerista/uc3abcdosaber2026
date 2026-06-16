from django.shortcuts import render, redirect
from .models import Aluno

# Create your views here.

def cadastrar_aluno(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        data_matricula = request.POST.get('data_matricula')
        data_saida = request.POST.get('data_saida')
        monitor = request.POST.get('monitor') == 'on'

        Aluno.objects.create(
            nome=nome,
            matricula=matricula,
            data_matricula=data_matricula,
            data_saida=data_saida,
            monitor=monitor
        )

        return redirect('aluno:listar')

    return render(request, 'aluno/cadastroAluno.html')

def listar_alunos(request):
    alunos = Aluno.objects.all()

    contexto = {
        'alunos': alunos
    }

    return render(request, 'aluno/listarAlunos.html', contexto)
