from django.db import models
from ..funcionario.models import Funcionario
from django.shortcuts import reverse, redirect
from django.utils.timezone import now


class HoraExtra(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    motivo = models.CharField(help_text="Informe o motivo", max_length=100)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizadas = models.BooleanField(default=False)
    criada_em = models.DateField(default=now)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('funcionario-update', args=[self.funcionario.id])
