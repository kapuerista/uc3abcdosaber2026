from django.urls import path
from . import views

app_name = 'instrutor'
urlpatterns = [    
    path('listar/', views.listar_instrutores, name='listar'),
    path('cadastrar/', views.cadastrar_instrutor, name='cadastrar'),
]