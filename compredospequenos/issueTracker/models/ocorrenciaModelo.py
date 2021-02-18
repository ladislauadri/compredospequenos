




# Core Django imports.
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import geocoder
import requests
from django.conf import settings


# Third party app imports
from ckeditor_uploader.fields import RichTextUploadingField
from smart_selects.db_fields import ChainedForeignKey
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField


# Blog application imports.
from blog.utils.blog_utils import count_words, read_time
from django_extensions.db.fields import AutoSlugField 

from issueTracker.models.ocorrenciaCategoriaModelo import OcorrenciaCategoria
from django.contrib.sites.models import Site
from localidades.models import Pais, Estado, Municipio
from blog.models.author_models import Profile

 

class Ocorrencia(models.Model):

    # Article status constants
    PUBLICO = "PUBLICO"
    PRIVADO = "PRIVADO"
    # CHOICES
    PROPRIEDADE = (
        (PUBLICO, 'Público'),
        (PRIVADO, 'Privado'),
    )


    # Article status constants
    AGUARDANDO = "AGUARDANDO"
    PROGRESSO = "PROGRESSO"
    CONCLUIDA = "CONCLUIDA"
    INCONCLUIDA = "INCONCLUIDA"
    # CHOICES
    ESTADO = (
        (AGUARDANDO, 'Não Respondida'),
        (PROGRESSO, 'Em tratativa'),
        (CONCLUIDA, 'Concluída'),
        (INCONCLUIDA, 'Iniciada, mas abandonada'),
    )

    # BLOG MODEL FIELDS
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(OcorrenciaCategoria, on_delete=models.CASCADE,
                                 related_name='ocorrencias')
    titulo = models.CharField(max_length=1500, null=False, blank=False)
    slug = AutoSlugField(populate_from=['id', 'titulo'], null=True, blank=True)
    reclamante = CurrentUserField()
    descrição = models.TextField(null=False, blank=False)
    localizacao = models.PointField(null=True, blank=True, srid=4326)
    endereco = models.CharField(max_length=1000, null=False, blank=False)
    numero = models.CharField(max_length=7, null=True, blank=True)
    complemento = models.CharField(max_length=1000, null=True, blank=True)
    bairro = models.CharField(max_length=1000, null=True, blank=True)
    # municipio = ChainedForeignKey(
    #     'localidades.Municipio',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='municipioOcorrencia',
    #     chained_field="estado",
    # chained_model_field="estado",
    #     show_all=False,
    #     auto_choose=False,
    #     sort=True
    #     )
    # estado = ChainedForeignKey(
    #     'localidades.Estado',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='estadoOcorrencia',
    #     chained_field="pais",
    #     chained_model_field="pais",
    #     show_all=False,
    #     auto_choose=False,
    #     sort=True
    #     )
    # pais = models.ForeignKey('localidades.Pais', on_delete=models.SET_NULL, null=True, related_name='paisOcorrencia')
    cep = models.CharField(max_length=9, null=True, blank=True )
    seguir = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='seguidores')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    dataConclusao = models.DateTimeField(null=True, blank=True)

    poder = models.CharField(max_length=10, choices=PROPRIEDADE,
                              default='PUBLICO')
    estadoDaOcorrencia = models.CharField(max_length=20, choices=ESTADO,
                              default='AGUARDANDO')
    anonimo = models.BooleanField(default=False)
    deletado = models.BooleanField(default=False)


    class Meta:
        unique_together = ("id", "titulo",)
        ordering = ('-dataCriacao',)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        api_key = '_NbpSVtDu2ymJoMb9a8hh5JLSYRiOk5s9Q9RW2fP6Y4'
        # q = self.endereco+' '+self.municipio.nome+', '+self.cep,
        # if self.endereco:
        #     q = self.endereco+' '+self.municipio.nome+', '+self.cep,
        strings = [self.endereco, ' ,', self.numero, ' ,',  self.complemento, ' ,',  self.bairro, ' ,',  self.cep]
        try:
            q = "".join([x for x in strings if x !=None])
            URL = "https://geocode.search.hereapi.com/v1/geocode?q={}&apikey={}".format(q, api_key)
        except Exception as e: # work on python 2.x
            strings.error('Há um erro no formulário'+ str(e))
            URL = []


        r = requests.get(url = URL)
        data = r.json()
        lng = data['items'][0]['position']['lat']
        lat = data['items'][0]['position']['lng']
        self.localizacao = Point([lat,lng])

        super(Ocorrencia, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('ocorrencias:detalhesDaOcorrencia', kwargs={'username': self.reclamante.username.lower(), 'slug': self.slug})


