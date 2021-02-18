from django.db import models
from django.urls import reverse
from django.utils import timezone

from cloudinary.models import CloudinaryField
from issueTracker.models.ocorrenciaModelo import Ocorrencia

class OcorrenciaFotos(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, related_name='imagens')
    imagem = CloudinaryField('ocorrenciaimg', blank=True, null=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True )

    def __str__ (self):
        return self.ocorrencia.titulo
    
    class Meta:
        verbose_name = 'Imagem da Ocorrência'
        verbose_name = 'Imagens das Ocorrências'