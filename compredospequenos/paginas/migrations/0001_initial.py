# Generated by Django 3.0.6 on 2021-01-31 02:21

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import fontawesome_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDasPaginas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodeDaCategoria', models.CharField(max_length=100)),
                ('imagem', fontawesome_5.fields.IconField(blank=True, max_length=60, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=['nodeDaCategoria', 'id'])),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomedaPagina', models.CharField(max_length=300)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagemDeCAbecalho', models.ImageField(blank=True, null=True, upload_to='paginas/%Y/%m/%d/')),
                ('ativo', models.BooleanField(default=False)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=['nomedaPagina', 'id'])),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paginas.CategoriaDasPaginas')),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]