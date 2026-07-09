from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [  
    path('listar/', views.listar_turmas, name='listar'),
    path('cadastrar/', views.cadastrar_turma, name='cadastrar'),
    path('ausencia/', views.registro_ausencia, name='ausencia'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('carregar_ausencia/', views.carregar_ausencia_alunos, name='ausencia_alunos'),
    path('registrar_ausencia/', views.registrar_ausencia, name='registrar_ausencia'),
]