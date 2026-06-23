from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('listar/', views.listar_alunos, name='listar'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),   
]