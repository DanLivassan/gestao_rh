from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from ..departamento.models import Departamento
from ..empresa.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Informe o nome")
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento,  blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse("funcionario-list")