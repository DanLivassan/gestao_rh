from django.db import models
from ..funcionario.models import Funcionario


class HoraExtra(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    motivo = models.CharField(help_text="Informe o motivo", max_length=100)
