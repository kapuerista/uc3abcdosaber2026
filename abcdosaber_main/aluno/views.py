from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

def cadastrar_aluno(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('aluno:listar')

    return render(request, 'aluno/cadastroAluno.html', {'form': form})


def listar_alunos(request):
    alunos = Aluno.objects.all()

    return render(request, 'aluno/listarAlunos.html', {
        'alunos': alunos
    })


def excluir(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('aluno:listar')