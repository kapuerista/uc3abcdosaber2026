from django.shortcuts import render, redirect
from tipodeatividade.models import Tipodeatividade


def listar(request):
    lista_tipodeatividade = Tipodeatividade.objects.all()

    contexto = {
        'tipodeatividade': lista_tipodeatividade
    }

    return render(
        request,
        'tipodeatividade/listarTiposAtividade.html',
        contexto
    )


def cadastrar(request):

    if request.method == 'POST':

        descricao = request.POST.get('descricao')

        Tipodeatividade.objects.create(
            descricao=descricao
        )

        return redirect('tipodeatividade:listar')

    return render(
        request,
        'tipodeatividade/cadastroTiposAtividade.html'
    )


def excluir(request, codigoTipoAtividade):

    try:
        tipo = Tipodeatividade.objects.get(pk=codigoTipoAtividade)
        tipo.delete()

    except Tipodeatividade.DoesNotExist:
        pass

    return redirect('tipodeatividade:listar')