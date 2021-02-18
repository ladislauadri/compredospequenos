from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from localidades.models import Pais, Estado, Municipio
from django_extensions.db.fields import AutoSlugField 
import geocoder
import requests
from smart_selects.db_fields import ChainedForeignKey
from ckeditor.fields import RichTextField
from fontawesome_5.fields import IconField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField

from django.urls import reverse
from django.contrib.sites.models import Site






class Anuncio(models.Model):
  id = models.AutoField(primary_key=True)
  nomeDoAnuncio = models.CharField(max_length=100)
  responsavel = CurrentUserField()
  tipoDeAnuncio = models.ForeignKey('TipoDeAnuncio', on_delete=models.SET_NULL, null=True)
  categoriaDoAnuncio = models.ForeignKey('CategoriaDoAnuncio', on_delete=models.SET_NULL, null=True)
  descricao = RichTextField()
  logo = models.ImageField(upload_to='logos/%Y/%m/%d/', blank=True, null=True)
  telefone = models.CharField(max_length=20, null=True, blank=True)
  whatsapp = models.CharField(max_length=20, null=True, blank=True)
  facebook = models.CharField(max_length=200, null=True, blank=True)
  instagram = models.CharField(max_length=200, null=True, blank=True)
  site = models.CharField(max_length=200, null=True, blank=True)
  localizacao = models.PointField(null=True, blank=True, srid=4326)
  endereco = models.CharField(max_length=200, null=True, blank=True)
  numero = models.CharField(max_length=7, null=True, blank=True)
  complemento = models.CharField(max_length=200, null=True, blank=True)
  municipio = ChainedForeignKey(
    'localidades.Municipio',
    on_delete=models.SET_NULL,
    null=True,
    related_name='municipio',
    chained_field="estado",
   chained_model_field="estado",
    show_all=False,
    auto_choose=False,
    sort=True
    )
  estado = ChainedForeignKey(
    'localidades.Estado',
    on_delete=models.SET_NULL,
    null=True,
    related_name='estado',
    chained_field="pais",
    chained_model_field="pais",
    show_all=False,
    auto_choose=False,
    sort=True
    )
  pais = models.ForeignKey('localidades.Pais', on_delete=models.SET_NULL, null=True, related_name='pais')
  cep = models.CharField(max_length=9, null=False, blank=False, )

  ativo = models.BooleanField(default=False)

  criado = models.DateTimeField(auto_now_add=True)
  atualizado = models.DateTimeField(auto_now=True)

  slug = AutoSlugField(populate_from=['id', 'nome'], null=True, blank=True)
  sites = models.ManyToManyField(Site, related_name='business')


  def __str__(self):
    return self.nome

  def save(self,  *args, **kwargs):
    api_key = '_NbpSVtDu2ymJoMb9a8hh5JLSYRiOk5s9Q9RW2fP6Y4'
    q = self.endereco+' '+self.numero+', '+self.municipio.nome+', '+self.cep,
    URL = "https://geocode.search.hereapi.com/v1/geocode?q={}&apikey={}".format(q, api_key)

    r = requests.get(url = URL)
    data = r.json()
    lng = data['items'][0]['position']['lat']
    lat = data['items'][0]['position']['lng']
    self.localizacao = Point([lat,lng])

 
    super(Anuncio, self).save( *args, **kwargs)

  def get_absolute_url(self):
    return reverse('anuncios:detalhesDoAnuncio', args=[str(self.slug)])


class TipoDeAnuncio(models.Model):
  ## Contém as Categorias das Empresas

  nodeDaCategoria = models.CharField(max_length=100)
  imagem = IconField(null=True, blank=True)

  slug = models.SlugField(blank=True, null=True)


  def save(self, *args, **kwargs):
    if not self.slug and self.nodeDaCategoria :
      self.slug = slugify(self.nodeDaCategoria)
    super(Categoria, self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'

  def __str__(self):
    return self.nodeDaCategoria



class CategoriaDoAnuncio(models.Model):
  ## Contém as Categorias das Empresas

  nodeDaCategoria = models.CharField(max_length=100)
  imagem = IconField(null=True, blank=True)

  slug = models.SlugField(blank=True, null=True)


  def save(self, *args, **kwargs):
    if not self.slug and self.nodeDaCategoria :
      self.slug = slugify(self.nodeDaCategoria)
    super(Categoria, self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'

  def __str__(self):
    return self.nodeDaCategoria


class GaleriaDeFotos(models.Model):
  ## Contém as Fotos dos Anuncios

  anuncio = models.ForeignKey('Anuncio', on_delete=models.SET_NULL, null=True)
  imagem = models.ImageField(upload_to='anuncios/', blank=True, null=True)
  
  class Meta:
    verbose_name = 'Galeria de Fotos'
    verbose_name_plural = 'Galeria de Fotos'

  def __str__(self):
    return self.anuncio.nome

