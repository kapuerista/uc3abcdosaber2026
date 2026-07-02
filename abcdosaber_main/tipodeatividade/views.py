from django.shortcuts import render, redirect
from tipodeatividade.forms import TiposdeAtividadeForm
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


def excluir(request, codigo):

    try:
        tipo_de_atividade = Tipodeatividade.objects.get(pk=codigo)
        tipo_de_atividade.delete()

    except Tipodeatividade.DoesNotExist:
        pass

    return redirect('tipodeatividade:listar')

def atualizar(request):
    if request.method == 'POST':
        
        form = TiposdeAtividadeForm(request.POST)
        if form.is_valid():
        
            dados_tipo_de_atividade = form.cleaned_data
        
            codigo = dados_tipo_de_atividade['codigo']
            tipo_de_atividade = Tipodeatividade.objects.get(pk=codigo)
        
            tipo_de_atividade.descricao = dados_tipo_de_atividade['descricao']
            tipo_de_atividade.save()
            
            return redirect('tipodeatividade:listar')
        
    return redirect('tipodeatividade:listar')

def carregar_tipodeativiade(request,codigo):
    #recuperar titulo a ser atualizado
    tipo_de_atividade = Tipodeatividade.objects.get(pk=codigo)
    contexto = {
        'tipodeatividade' : tipo_de_atividade
    }
    
    return render(request, 'tipodeatividade/atualizarTiposAtividade.html', context=contexto)