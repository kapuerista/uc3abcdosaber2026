from multiprocessing import context
from django import forms
from django.shortcuts import render, redirect


from instrutor.forms import InstrutorForm
from instrutor.models import Instrutor
from titulo.models import Titulo

# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        "instrutores": lista_instrutor
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

def cadastrar(request):
    if request.method == "POST":
        form_instrutor = InstrutorForm(request.POST)
        if form_instrutor.is_valid():
            dados = form_instrutor.cleaned_data

            instrutor = Instrutor(
                rg=dados['rg'],
                nome=dados['nome'],
                data_nascimento=dados['data_nascimento'],
                ddd=dados['ddd'],
                telefone=dados['telefone'],
                codigo_titulo=dados['codigo_titulo']
            )
            instrutor.save()
            return redirect('instrutor:listar')

    else:
        form_instrutor = InstrutorForm()

    return render(request, 'instrutor/cadastroInstrutor.html', {
        "form": form_instrutor
    })

def carregar_cadastro(request):
    lista_titulos = Titulo.objecs.all()
    contexto= {
        "titulos":lista_titulos
    }
    
    return render(request, 'instrutor/cadastroInstrutor.html', context=contexto)

    