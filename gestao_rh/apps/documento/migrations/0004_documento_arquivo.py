# Generated by Django 3.0.8 on 2020-07-19 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0003_auto_20200718_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]
