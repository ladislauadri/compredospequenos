from django.urls import path, re_path, include, reverse
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.views.generic import TemplateView

from .views import OcorrenciaView, OcorrenciaDetailView, OcorrenciaCreate







app_name = 'ocorrencias'



urlpatterns = [ 
  path('', OcorrenciaView.as_view(), name='ListaDeOcorrencias'),
  path('o/<slug>/', OcorrenciaDetailView.as_view(), name='detalhesDaOcorrencia'),
  path('criar/', OcorrenciaCreate.as_view(), name='criarOcorrencia'),
 
]