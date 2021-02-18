from django.db import models
from django.conf import settings

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from localidades.models import Pais, Estado, Municipio
from django_extensions.db.fields import AutoSlugField
import geocoder
from smart_selects.db_fields import ChainedForeignKey
from ckeditor.fields import RichTextField
from fontawesome_5.fields import IconField
from django.conf import settings


from django.urls import reverse






class Pagina(models.Model):


    id = models.AutoField(primary_key=True)
    nomedaPagina = models.CharField(max_length=300)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey('CategoriaDasPaginas', on_delete=models.SET_NULL, null=True)
    conteudo = RichTextField()
    imagemDeCAbecalho = models.ImageField(upload_to='paginas/%Y/%m/%d/', blank=True, null=True)

    ativo = models.BooleanField(default=False)

   

    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    slug = AutoSlugField(populate_from=['nomedaPagina', 'id'], null=True, blank=True)

    def __str__(self):
      return self.nomedaPagina

    def get_absolute_url(self):
      return reverse('paginas:DetalhesDaPagina', args=[str(self.slug)])



class CategoriaDasPaginas(models.Model):

  nodeDaCategoria = models.CharField(max_length=100)
  imagem = IconField(null=True, blank=True)

  slug = AutoSlugField(populate_from=['nodeDaCategoria', 'id'], null=True, blank=True)


  
  class Meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'

  def __str__(self):
    return self.nodeDaCategoria
