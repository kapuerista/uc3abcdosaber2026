from django.urls import path
from . import views

app_name = 'tipodeatividade'

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigoTipoAtividade>/', views.excluir, name='excluir'),
    path('atualizar/', views.atualizar, name='atualizar_titulo'),
    path('carregar_tipodeatividade/<int:codigo>', views.carregar_tipodeativiade, name='carregar_atividade'),
]
    
    