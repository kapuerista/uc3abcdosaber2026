from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_view(request):
    return HttpResponse( "<p> Mnha view do app Títulos </p>")

def show_template(request):
    return HttpResponse( "<p> Minha view do app Títulos usando template </p>")

def listar_exemplo(request):
    pagina='Olá'
    return HttpResponse(pagina)

def abc(request):
    pagina = 'ABC'
    return HttpResponse(pagina)

def index(request):
    return render(request, 'index.html')










