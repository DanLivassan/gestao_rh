# Generated by Django 3.0.8 on 2020-07-26 14:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0007_auto_20200725_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaextra',
            name='criada_em',
            field=models.DateField(default=datetime.datetime(2020, 7, 26, 14, 23, 34, 966613, tzinfo=utc)),
        ),
    ]
