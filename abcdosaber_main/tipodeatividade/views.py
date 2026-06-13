from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import render
from tipodeatividade.models import Tipodeatividade

# Create your views here.
def listar (request):
    lista_tipodeatividade = Tipodeatividade.objects.all()
    contexto = {
        'tipodeatividade': lista_tipodeatividade
    }
    return render(request, 'tipodeatividade/listarTiposAtividade.html', context=contexto)

def cadastrar(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')