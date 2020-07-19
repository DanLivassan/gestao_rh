from django.db import models
from ..empresa.models import Empresa


class Departamento(models.Model):

    nome = models.CharField(help_text="Insira o nome", max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

