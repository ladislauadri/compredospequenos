from django.urls import path, re_path, include, reverse
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from homepage.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView
from homepage.views import SitemapXMLView

from locais.models import Local, CategoriaDoLocal
from localidades.models import Pais, Estado, Municipio
from promocoes.models import Promocoes, CategoriaPromocional
from paginas.models import Pagina, CategoriaDasPaginas
from blog.models import ArtigosBlog, CategoriaDosArtigos






app_name = 'home'



urlpatterns = [ 
  path('ckeditor', include('ckeditor_uploader.urls')),

 
]