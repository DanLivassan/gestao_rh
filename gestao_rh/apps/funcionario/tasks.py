# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Funcionario

from django.core.mail import send_mail

@shared_task
def send_email_app(Assunto):
    total = Funcionario.objects.all().count()

    send_mail(
        Assunto,
        'Você tem {} funcionarios'.format(total),
        'oliveira.xc@msn.com',
        ['daniloxc@msn.com'],
        fail_silently=False,
    )
    return True

