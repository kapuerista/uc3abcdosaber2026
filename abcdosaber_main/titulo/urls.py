from django.urls import path
from . import views

app_name = 'titulo'

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('cadastro/', views.cadastrar, name= 'cadastro'),
    path('excluir/<int:codigoTitulo>', views.excluir, name='excluir_titulo'),
        
]