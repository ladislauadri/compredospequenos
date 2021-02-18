from django.db import models
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField



class Pais(models.Model):
    nome = models.CharField(max_length=30, unique=True)
      
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nome

class Estado(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="estados")
    nome = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from=['id', 'nome'], null=True, blank=True)


    def __str__(self):
        return self.nome

class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="municipios")
    nome = models.CharField(max_length=100, )
    slug = AutoSlugField(populate_from=['id', 'nome'], null=True, blank=True)


    def __str__(self):
        return self.nome
