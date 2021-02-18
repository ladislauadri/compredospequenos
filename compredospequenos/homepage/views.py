from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
import requests
import json
import urllib
from queryset_sequence import QuerySetSequence

from ipware import get_client_ip

from locais.models import Local, CategoriaDoLocal
from localidades.models import Pais, Estado, Municipio
# from promocoes.models import Promocoes, CategoriaPromocional
from paginas.models import Pagina, CategoriaDasPaginas
from posts.models import Post
from blog.models.article_models import Article


class HomepageView(ListView):
    model = Local
    template_name = 'homepage/home.html'


    

    def get_context_data(self, **kwargs):
      # client_ip, is_routable = get_client_ip(self.request)
      # api_key = '85333f4c26c48b675004450cdf8575d1'
      # q = client_ip
      # URL = "http://api.ipstack.com/{}?access_key={}&format=1".format(q, api_key)
      # response = urllib.request.urlopen(URL)
      # data = json.loads(response.read())
      query = QuerySetSequence(Local.objects.all(), Post.objects.all(), Article.objects.all()).order_by('-createdAt')



      
      context = super().get_context_data(**kwargs)
      context['listaDeLocais'] = Local.objects.all().filter(ativo=True)[:5]
      context['listaDeArtigos'] = Article.objects.all().filter()[:10]
      context['listas'] = query
      # context['url'] = data
      # context['paginas'] = Pagina.objects.filter(ativo=True)
      return context
    

class SitemapXMLView(TemplateView):
  # template_name = 'sitemap/sitemapxml.html'
  content_type = 'application/xml'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['artigos'] = ArtigosBlog.objects.filter(status=1)
      context['locais'] = Local.objects.filter(ativo=True)
      context['paginas'] = Pagina.objects.filter(ativo=True)
      return context
  