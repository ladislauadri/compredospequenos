from django.shortcuts import render, get_object_or_404, redirect


from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pagina,CategoriaDasPaginas
# from promocoes.models import Promocoes
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.http import Http404

class ListaDePagina(ListView): 
    model = Pagina
    template_name = 'pagina/listadepaginas.html'
    context_object_name = 'paginas'
    paginate_by = 10
    def get_queryset(self):
        return super(ListaDePagina, self).get_queryset().filter(ativo=True)
    def get_context_data(self, **kwargs):
        context = super(ListaDePagina, self).get_context_data(**kwargs)
        paginas = self.get_queryset()
        page = self.request.GET.get('page')
        context['paginas'] = paginas
        return context


class DetalhesDaPagina(DetailView): 
    model = Pagina
    template_name = 'pagina/detalhesdapagina.html'
    context_object_name = 'pagina'
    queryset = Pagina.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj