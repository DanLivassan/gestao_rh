# Generated by Django 3.0.8 on 2020-07-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_horaextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]