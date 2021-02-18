# Generated by Django 3.0.6 on 2021-02-10 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0004_auto_20210208_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoDoLocal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identificador', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('TELEFONE', 'Telefone'), ('WHATSAPP', 'Whatsapp'), ('FACEBOOK', 'Facebook'), ('INSTAGRAM', 'Instagram'), ('LINKEDIN', 'Linkedin'), ('EMAIL', 'Email'), ('SITE', 'Site'), ('TIKTOK', 'TikTok'), ('TWITTER', 'Twitter'), ('YOUTUBE', 'Youtube'), ('TELEGRAM', 'Telegram'), ('DISCORD', 'Discord'), ('TWITCH', 'Twitch'), ('SNAPCHAT', 'Snapchat')], default='TELEFONE', max_length=10)),
                ('valor', models.CharField(blank=True, max_length=1000, null=True)),
                ('aprovado', models.BooleanField(default=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'db_table': 'contatoLocal',
                'managed': True,
            },
        ),
    ]