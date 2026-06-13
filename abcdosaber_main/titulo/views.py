from django.http import HttpResponse
from django.shortcuts import render, redirect
from titulo.models import Titulo

# Create your views here.
def listar(request):
    lista_titulos= Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }    
    return render(request, 'titulo/listarTitulos.html', context=contexto)
    

def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')

def excluir(request, codigoTitulo):
    try:
        titulo = titulo.objects.get(pk=codigoTitulo)
        titulo.delete()
    except Titulo.DoesNotExist:
        pass
        
    return redirect('titulo:listar')
















