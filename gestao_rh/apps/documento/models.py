from django.db import models
from ..funcionario.models import Funcionario


class Documento(models.Model):

    nome = models.CharField(max_length=120, help_text="Nome do documento")
    propriedade_de = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.nome

