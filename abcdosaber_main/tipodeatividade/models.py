from django.db import models

# Create your models here.
class Tipodeatividade(models.Model):
    codigo = models.AutoField(
        primary_key=True,
        help_text='código de Tipos de Atividade'
    )
    
    descricao= models.CharField(
        max_length=70,
        null=False,
        help_text='Informe a descrição do tipos de atividade'
    )
    def __str__(self):
        return f'{self.codigo} {self.descricao}'