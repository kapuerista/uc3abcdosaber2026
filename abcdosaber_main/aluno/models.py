from django.db import models

# Create your models here.

from django.db import models

class Aluno(models.Model):

    matricula = models.AutoField(primary_key=True)

    nome = models.CharField(
        max_length=100,
        null=False,
        help_text="Informe o nome do aluno"
    )

    data_matricula = models.DateField()

    data_saida = models.DateField(
        null=True,
        blank=True,
        help_text="Informe a data final de matrícula do aluno"
    )

    monitor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.matricula} - {self.nome}"
