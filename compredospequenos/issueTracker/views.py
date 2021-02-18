from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
import requests
import json
import urllib

from ipware import get_client_ip

from issueTracker.models.ocorrenciaModelo import Ocorrencia
from django.views.generic.edit import FormView
from issueTracker.forms import OcorrenciaForm

class OcorrenciaView(ListView):
    model = Ocorrencia
    template_name = 'ocorrencias/ocorrenciaLista.html'
    

    def get_context_data(self, **kwargs):
      # client_ip, is_routable = get_client_ip(self.request)
      # api_key = '85333f4c26c48b675004450cdf8575d1'
      # q = client_ip
      # URL = "http://api.ipstack.com/{}?access_key={}&format=1".format(q, api_key)
      # response = urllib.request.urlopen(URL)
      # data = json.loads(response.read())


      
      context = super().get_context_data(**kwargs)
      context['listaDeOcorrencias'] = Ocorrencia.objects.all()
      context['apiKey'] = 'Sco_-HzVL-53Drcv-N4lRio6YmYRJN9Bj7UmgbAB80I'
      # context['paginas'] = Pagina.objects.filter(ativo=True)
      return context

class OcorrenciaCreate(CreateView):
    model = Ocorrencia
    template_name = 'ocorrencias/ocorrenciaCriar.html'
    form_class = OcorrenciaForm
    success_url = reverse_lazy('ocorrencias:ListaDeOcorrencias')

class OcorrenciaUpdate(UpdateView):
    model = Ocorrencia
    fields = '__all__'

class OcorrenciaDelete(DeleteView):
    model = Ocorrencia
    success_url = reverse_lazy('ListaDeOcorrencias')

class OcorrenciaDetailView(DetailView):
    model = Ocorrencia
    template_name = 'ocorrencias/ocorrenciaDetalhe.html'
    query_pk_and_slug = True
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    

    def get_context_data(self, **kwargs):
        # kwargs['related_articles'] = self.object.tags.similar_objects()[:4]
        kwargs['ocorrencia'] = self.object
        # kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)

    




