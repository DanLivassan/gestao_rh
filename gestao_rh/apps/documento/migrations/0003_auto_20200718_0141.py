# Generated by Django 3.0.8 on 2020-07-18 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0003_auto_20200718_0139'),
        ('documento', '0002_documento_propriedade_de'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='propriedade_de',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionario.Funcionario'),
            preserve_default=False,
        ),
    ]
