from django.urls import path
from . import views

urlpatterns = [
    path('', views.tipodeatividade , name='tipodeatividade'),    
    
]