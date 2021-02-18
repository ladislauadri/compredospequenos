import geocoder
import requests
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField 
from django.urls import reverse
from django.contrib.sites.models import Site
from smart_selects.db_fields import ChainedForeignKey
from ckeditor.fields import RichTextField
from fontawesome_5.fields import IconField
from model_clone import CloneMixin

from django.conf import settings

from localidades.models import Pais, Estado, Municipio

# Article status constants
TELEFONE = "TELEFONE"
WHATSAPP = "WHATSAPP"
FACEBOOK = "FACEBOOK"
INSTAGRAM = "INSTAGRAM"
LINKEDIN = "LINKEDIN"
EMAIL = "EMAIL"
SITE = "SITE"
TIKTOK = "TIKTOK"
TWITTER = "TWITTER"
YOUTUBE = "YOUTUBE"
TELEGRAM = "TELEGRAM"
DISCORD = "DISCORD"
TWITCH = "TWITCH"
SNAPCHAT = "SNAPCHAT"

# CHOICES
CONTACT_CHOICES = (
        (TELEFONE, 'Telefone'),
        (WHATSAPP, 'Whatsapp'),
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (LINKEDIN, 'Linkedin'),
        (EMAIL, 'Email'),
        (SITE, 'Site'),
        (TIKTOK, 'TikTok'),
        (TWITTER, 'Twitter'),
        (YOUTUBE, 'Youtube'),
        (TELEGRAM, 'Telegram'),
        (DISCORD, 'Discord'),
        (TWITCH, 'Twitch'),
        (SNAPCHAT, 'Snapchat'),
)


class Local(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=100)
  responsavel = CurrentUserField()
  categoria = models.ForeignKey('CategoriaDolocal', on_delete=models.SET_NULL, null=True)
  descricao = models.TextField(max_length=10000)
  logo = models.ImageField(upload_to='logos/%Y/%m/%d/', blank=True, null=True)
  telefone = models.CharField(max_length=20, null=True, blank=True)
  whatsapp = models.CharField(max_length=20, null=True, blank=True)
  facebook = models.CharField(max_length=200, null=True, blank=True)
  instagram = models.CharField(max_length=200, null=True, blank=True)
  site = models.CharField(max_length=1000, null=True, blank=True)
  email = models.CharField(max_length=1000, null=True, blank=True)
  # localizacao = models.PointField(null=True, blank=True, srid=4326)
  # endereco = models.CharField(max_length=1000, null=True, blank=True)
  # numero = models.CharField(max_length=7, null=True, blank=True)
  # complemento = models.CharField(max_length=200, null=True, blank=True)
  # municipio = ChainedForeignKey(
  #   'localidades.Municipio',
  #   on_delete=models.SET_NULL,
  #   null=True,
  #   related_name='municipio',
  #   chained_field="estado",
  #  chained_model_field="estado",
  #   show_all=False,
  #   auto_choose=False,
  #   sort=True
  #   )
  # estado = ChainedForeignKey(
  #   'localidades.Estado',
  #   on_delete=models.SET_NULL,
  #   null=True,
  #   related_name='estado',
  #   chained_field="pais",
  #   chained_model_field="pais",
  #   show_all=False,
  #   auto_choose=False,
  #   sort=True
  #   )
  # pais = models.ForeignKey('localidades.Pais', on_delete=models.SET_NULL, null=True, related_name='pais')
  # cep = models.CharField(max_length=9, null=False, blank=False, )

  ativo = models.BooleanField(default=True)

  # dataCriacao = models.DateTimeField(auto_now_add=True)
  # dataAtualizacao = models.DateTimeField(auto_now=True)
  # dataPublicacao = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)


  slug = AutoSlugField(populate_from=['id', 'nome'], null=True, blank=True)
  sites = models.ManyToManyField(Site, related_name='site')


  def __str__(self):
    return self.nome

  def save(self,  *args, **kwargs):
    if not self.slug and self.nome :
          self.slug = slugify(self.nome)
    super(Local, self).save( *args, **kwargs)

  def get_absolute_url(self):
    return reverse('locais:detalhesDoLocal', args=[str(self.slug)])
  
  class Meta:
    db_table = 'local'
    managed = True
    verbose_name = 'Local'
    verbose_name_plural = 'Locais'

    
class LocalEndereco(models.Model):
  id = models.AutoField(primary_key=True)
  local = models.ForeignKey('Local', on_delete=models.SET_NULL, null=True, related_name='estabelecimento')
  localizacao = models.PointField(null=True, blank=True, srid=4326)
  endereco = models.CharField(max_length=1000, null=False, blank=False,)
  numero = models.CharField(max_length=7, null=True, blank=True)
  complemento = models.CharField(max_length=200, null=True, blank=True)
  bairro = models.CharField(max_length=1000, null=True, blank=True)
  municipio = models.CharField(max_length=1000, null=True, blank=True)
  estado = models.CharField(max_length=1000, null=True, blank=True)
  pais = models.CharField(max_length=1000, null=True, blank=True)
  cep = models.CharField(max_length=9, null=True, blank=True)

  ativo = models.BooleanField(default=True)

  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)


  slug = AutoSlugField(populate_from=['id'], null=True, blank=True)


  def __str__(self):
    return self.local.nome

  def save(self,  *args, **kwargs):
    api_key = '_NbpSVtDu2ymJoMb9a8hh5JLSYRiOk5s9Q9RW2fP6Y4'
    # q = self.endereco+' '+self.numero+', '+self.municipio.nome+', '+self.cep,
    # URL = "https://geocode.search.hereapi.com/v1/geocode?q={}&apikey={}".format(q, api_key)
    strings = [self.endereco, ' ,', self.numero, ' ,',  self.complemento, ' ,',  self.bairro, ' ,',  self.municipio, ' ,',  self.estado, ' ,',  self.pais, ' ,',  self.cep]
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
    bairro = data['items'][0]['address']['district']
    municipio = data['items'][0]['address']['city']
    estado = data['items'][0]['address']['state']
    pais = data['items'][0]['address']['countryName']
    cep = data['items'][0]['address']['postalCode']
    
    self.localizacao = Point([lat,lng])
    if self.bairro == None:
          self.bairro = bairro
    if self.municipio == None:
          self.municipio = municipio
    if self.estado == None:
          self.estado = estado
    if self.pais == None:
          self.pais = pais
    if self.cep == None:
          self.cep = cep

 
    super(LocalEndereco, self).save( *args, **kwargs)

  def get_absolute_url(self):
    return reverse('locais:detalhesDoLocal', args=[str(self.slug)])
  
  class Meta:
    db_table = 'endereco'
    managed = True
    verbose_name = 'Endereço'
    verbose_name_plural = 'Endereços'




class ContatoDoLocal(models.Model):
  ## Contém as Categorias das Empresas
  id = models.AutoField(primary_key=True)
  local = models.ForeignKey('Local', on_delete=models.SET_NULL, null=True, related_name='contatosDoLocal')

  tipo = models.CharField(max_length=10, choices=CONTACT_CHOICES,
                              default='TELEFONE')
  valor = models.CharField(max_length=1000, null=True, blank=True)
  
  aprovado = models.BooleanField(default=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)


  def save(self, *args, **kwargs):
    super(ContatoDoLocal, self).save(*args, **kwargs)

  class Meta:
    db_table = 'contatoLocal'
    managed = True
    verbose_name = 'Contato'
    verbose_name_plural = 'Contatos'

  def __str__(self):
    return f"Contato de {self.tipo} de {self.local.nome}" 



class CategoriaDoLocal(models.Model):
  ## Contém as Categorias das Empresas
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=100)
  categoriaBase = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
  icone = IconField(null=True, blank=True)
  imagem = models.ImageField(default='category-default.jpg',
                              upload_to='locais/categoria/imagem/%Y/%m/%d/')
  slug = models.SlugField(blank=True, null=True)
  aprovado = models.BooleanField(default=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)


  def save(self, *args, **kwargs):
    if not self.slug and self.nome :
      self.slug = slugify(self.nome)
    super(CategoriaDoLocal, self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'

  def __str__(self):
    return self.nome






class TipoDeLocal(models.Model):
  ## Contém as Categorias das Empresas
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=100)
  icone = IconField(null=True, blank=True)
  imagem = models.ImageField(default='category-default.jpg',
                              upload_to='locais/tipodelocal/imagem/%Y/%m/%d/')
  slug = models.SlugField(blank=True, null=True)
  aprovado = models.BooleanField(default=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)


  def save(self, *args, **kwargs):
    if not self.slug and self.nome :
      self.slug = slugify(self.nome)
    super(TipoDeLocal, self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'Tipo de Local'
    verbose_name_plural = 'Tipos de Locais'

  def __str__(self):
    return self.nome

class GaleriaDeFotosDosLocais(models.Model):
  ## Contém as Fotos dos Anuncios
  id =  models.AutoField(primary_key=True)
  local = models.ForeignKey('Local', on_delete=models.SET_NULL, null=True)
  imagem = models.ImageField(upload_to='locais/fotos/%Y/%m/%d/', blank=True, null=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name = 'Galeria de Fotos'
    verbose_name_plural = 'Galeria de Fotos'

  def __str__(self):
    return self.local.nome

class Promocoes(models.Model):
      ## Contém as Fotos dos Anuncios
  id =  models.AutoField(primary_key=True)
  nome = models.CharField(max_length=200)
  precoReal = models.CharField(max_length=7)
  precoPromocional = models.CharField(max_length=7)
  linkDeCompra = models.CharField(max_length=200)
  local = models.ForeignKey('Local', on_delete=models.SET_NULL, null=True)
  info = RichTextField(blank=True, null=True)
  categorias = models.ManyToManyField('CategoriaPromocional', through='BaseDePromocoes')

  fotoDoLocal = models.ImageField(upload_to='promo/%Y/%m/%d/', blank=True, null=True)
  prazoDaOferta = models.DateField() 
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)
  slug = AutoSlugField(populate_from=['nome', 'id'], null=True, blank=True)
 
  
  class Meta:
    verbose_name = 'Promoção'
    verbose_name_plural = 'Promoções'

  def __str__(self):
    return '%s (%s)' %(self.id, self.nome)


class CategoriaPromocional(models.Model):
      ## Contém as Categorias das Empresas
  id =  models.AutoField(primary_key=True)
  nome = models.CharField(max_length=200)
  imagem = IconField(null=True, blank=True)
  promocao = models.ManyToManyField('Promocoes', through='BaseDePromocoes')

  slug = AutoSlugField(populate_from=['nome', 'id'], null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)


  class Meta:
    verbose_name = 'Categoria Promocional'
    verbose_name_plural = 'Categorias Promocionais'

  def __str__(self):
    return self.nome

class BaseDePromocoes(models.Model):
  id =  models.AutoField(primary_key=True)
  categorias = models.ForeignKey('CategoriaPromocional', on_delete=models.SET_NULL, null=True, blank=True)
  promocao = models.ForeignKey('Promocoes', on_delete=models.SET_NULL, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  publishedAt = models.DateTimeField(auto_now=True)