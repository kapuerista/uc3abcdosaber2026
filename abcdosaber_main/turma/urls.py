from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [  
    path('listar/', views.listar_turmas, name='listar'),
    path('cadastrar/', views.cadastrar_turma, name='cadastrar'),
    path('ausencia/', views.registro_ausencia, name='ausencia'),
    path('construcao/', views.pagina_em_construcao, name='construcao'),
]