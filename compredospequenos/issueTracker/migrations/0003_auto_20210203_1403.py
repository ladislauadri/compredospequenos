# Generated by Django 3.0.6 on 2021-02-03 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issueTracker', '0002_auto_20210203_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ocorrenciacategoria',
            options={'ordering': ['nome'], 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='pais',
        ),
    ]