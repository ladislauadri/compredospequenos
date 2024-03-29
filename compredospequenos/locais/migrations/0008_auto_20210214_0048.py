# Generated by Django 3.0.6 on 2021-02-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0007_remove_contatodolocal_identificador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basedepromocoes',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='basedepromocoes',
            old_name='dataAtualizacao',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='categoriadolocal',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='categoriadolocal',
            old_name='dataAtualizacao',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='categoriapromocional',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='categoriapromocional',
            old_name='dataAtualizacao',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='contatodolocal',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='contatodolocal',
            old_name='dataAtualizacao',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='galeriadefotosdoslocais',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='galeriadefotosdoslocais',
            old_name='dataAtualizacao',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='local',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='local',
            old_name='dataPublicacao',
            new_name='publishedAt',
        ),
        migrations.RenameField(
            model_name='localendereco',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='localendereco',
            old_name='dataPublicacao',
            new_name='publishedAt',
        ),
        migrations.RenameField(
            model_name='promocoes',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='promocoes',
            old_name='dataAtualizacao',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='tipodelocal',
            old_name='dataCriacao',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='tipodelocal',
            old_name='dataAtualizacao',
            new_name='updatedAt',
        ),
        migrations.RemoveField(
            model_name='local',
            name='dataAtualizacao',
        ),
        migrations.RemoveField(
            model_name='localendereco',
            name='dataAtualizacao',
        ),
        migrations.AddField(
            model_name='basedepromocoes',
            name='publishedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='categoriadolocal',
            name='publishedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='categoriapromocional',
            name='publishedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contatodolocal',
            name='publishedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='galeriadefotosdoslocais',
            name='publishedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='local',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='localendereco',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='promocoes',
            name='publishedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tipodelocal',
            name='publishedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
