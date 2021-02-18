# Core Django imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Third party app imports
from taggit_selectize.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Blog application imports.
from app.blog.utils.blog_utils import count_words, read_time
from app.blog.models.category_models import Category
from django.contrib.sites.models import Site


class Artigo(models.Model):

    # Article status constants
    RASCUNHO = "RASCUNHO"
    PUBLICADO = "PUBLICADO"

    # CHOICES
    STATUS_ESCOLHAS = (
        (RASCUNHO, 'Rascunho'),
        (PUBLICADO, 'Publicado'),
    )

    # BLOG MODEL FIELDS
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
                                 related_name='artigos', null=True)
    titulo = models.CharField(max_length=1500, null=False, blank=False)
    subtitulo = models.CharField(max_length=1500, null=True, blank=True)
    slug = models.SlugField(max_length=1500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='artigos')
    imagem = models.ImageField(default='article-default.jpg',
                              upload_to='article_pics')
    imagemCredito = models.CharField(max_length=1000, null=True, blank=True)
    conteudo = RichTextUploadingField(blank=True)
    tags = TaggableManager(blank=True)
    dataPublicacao = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_ESCOLHAS,
                              default='RASCUNHO')
    visualizacoes = models.PositiveIntegerField(default=0)
    contagemDePalavras = models.CharField(max_length=50, default=0)
    tempoDeLeitura = models.CharField(max_length=50, default=0)
    excluido = models.BooleanField(default=False)

    sites = models.ManyToManyField(Site, related_name='artigos')

    class Meta:
        unique_together = ("titulo",)
        ordering = ('-dataPublicacao',)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        self.contagemDePalavras = contagemDePalavras(self.conteudo)
        self.tempoDeLeitura = tempoDeLeitura(self.conteudo)
        super(Artigo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'username': self.author.username.lower(), 'slug': self.slug})


