# Generated by Django 3.0.6 on 2021-02-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0002_auto_20210207_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='descricao',
            field=models.TextField(max_length=10000),
        ),
    ]
