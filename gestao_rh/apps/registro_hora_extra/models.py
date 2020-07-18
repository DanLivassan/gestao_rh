from django.db import models


class HoraExtra(models.Model):
    motivo = models.CharField(help_text="Informe o motivo", max_length=100)
