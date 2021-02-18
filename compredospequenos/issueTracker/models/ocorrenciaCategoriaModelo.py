# Core Django imports.
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class OcorrenciaCategoria(models.Model):

    nome = models.CharField(max_length=1000, null=False, blank=False)
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(default='category-default.jpg',
                              upload_to='ocorrencias/categorias')
    aprovada = models.BooleanField(default=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome, allow_unicode=True)
        super(OcorrenciaCategoria, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home',
                       kwargs={'slug': self.slug})
