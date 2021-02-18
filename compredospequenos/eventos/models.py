# Core Django imports.
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Third party app imports
from taggit_selectize.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Blog application imports.
from blog.models.category_models import Category
from django.contrib.sites.models import Site


class Article(models.Model):

    # BLOG MODEL FIELDS
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(CategoriaDeEventos, on_delete=models.SET_NULL,
                                 related_name='eventos', null=True)
    nome = models.CharField(max_length=1500, null=False, blank=False)
    slug = models.SlugField(max_length=1500)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='evento')
    imagem = models.ImageField(default='article-default.jpg',
                              upload_to='imagemDoEvento')
    participantes = models.ManyToManyField(User, related_name='participantes', blank=True)
    participantes = models.ManyToManyField(User, related_name='participantes', blank=True)
    detalhes = RichTextUploadingField(blank=True)
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
    tags = TaggableManager(blank=True)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    count_words = models.CharField(max_length=50, default=0)
    read_time = models.CharField(max_length=50, default=0)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.count_words = count_words(self.body)
        self.read_time = read_time(self.body)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'username': self.author.username.lower(), 'slug': self.slug})





class CategoriaDeEventos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    image = models.ImageField(default='category-default.jpg',
                              upload_to='categoriasdeeventos')
    aprovado = models.BooleanField(default=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('nome',)
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('blog:category_articles',
    #                    kwargs={'slug': self.slug})


