from django.shortcuts import render, redirect
from .models import (
  Local,
  LocalEndereco,
  CategoriaDoLocal,
  ContatoDoLocal,
  TipoDeLocal,
  GaleriaDeFotosDosLocais,
  Promocoes,
  CategoriaPromocional,
  BaseDePromocoes
)
from localidades.models import (
  Pais, 
  Estado, 
  Municipio)
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView,
  TemplateView)
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest  
from django.views import generic
from .forms import AdForm 
from django.views.generic.edit import CreateView, FormView
from braces.views import SelectRelatedMixin
from django.utils import timezone
import geocoder
 

class ListaDeLocaisView(ListView):
    
    model = Local
    paginate_by = 100  # if pagination is desired
    context_object_name = 'tipoDeLocal'
    template_name = 'local/listadelocais.html'

    def get_context_data(self, **kwargs):
        kwargs['listaDeLocais'] = LocalEndereco.objects.all().filter(ativo=True).order_by('-dataCriacao')
        # kwargs['estabelecimentos'] = LocalEndereco.objects.filter(local__pk=self.pk)
        # kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)


class DetalhesDoLocalView(DetailView):
    model = Local
    template_name = 'local/detalhesdolocal.html'
    query_pk_and_slug = True
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        # kwargs['related_articles'] = self.object.tags.similar_objects()[:4]
        kwargs['detalhesDoLocal'] = self.object
        kwargs['listaDeLocais'] = LocalEndereco.objects.all().filter(ativo=True, local__slug=self.kwargs['slug']).order_by('-dataCriacao')
        kwargs['listaDeLinks'] = ContatoDoLocal.objects.all().filter(aprovado=True, local__slug=self.kwargs['slug']).order_by('-dataCriacao')
        # kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)

 
def listadelocais(request, slugDaCategoria=None):
    categoria = None
    listadelocais = Local.objects.all().filter(ativo=True).order_by('-dataCriacao')
    listadecategorias = CategoriaDoLocal.objects.annotate(todasAsCategorias=Count('local'))
    teste = request.META['HTTP_X_FORWARDED_FOR'] 
    g = geocoder.ipinfo(teste)



    if slugDaCategoria :
      categoria = CategoriaDoLocal.objects.get(slug=slugDaCategoria)
      listadelocais = listadelocais.filter(categoria=categoria)

    itemDaPesquisa = request.GET.get('busca')
    if itemDaPesquisa:
      listadelocais = listadelocais.filter(
        Q(nome__icontains = itemDaPesquisa) |
        Q(descricao__icontains = itemDaPesquisa) |
        Q(tipoDeItem__icontains = itemDaPesquisa) |
        Q(slug__icontains = itemDaPesquisa) |
        Q(categoria__nodeDaCategoria__icontains = itemDaPesquisa)
      )
    paginator = Paginator(listadelocais, 10) # Show 25 contacts per page.
    page = request.GET.get('page')
    listadelocais = paginator.get_page(page)

  

    template = 'local/listadelocais.html'
    context = {
      'listaDeLocais' : listadelocais , 
      'listaDeCategorias' : listadecategorias, 
      'categoria' : categoria, 
      'teste': g.city,
      }
    return render(request , template, context )




def listadelocais2(request, slugDaCategoria=None):
    teste = request.META['HTTP_X_FORWARDED_FOR'] 
    g = geocoder.ipinfo(teste)
    categoria = None
    listadelocais = Local.objects.all().filter( municipio__nome__contains=g.city )
    listadecategorias = CategoriaDoLocal.objects.annotate(todasAsCategorias=Count('local'))





    if slugDaCategoria :
      categoria = CategoriaDoLocal.objects.get(slug=slugDaCategoria)
      listadelocais = listadelocais.filter(categoria=categoria)

    itemDaPesquisa = request.GET.get('busca')
    if itemDaPesquisa:
      listadelocais = listadelocais.filter(
        Q(nome__icontains = itemDaPesquisa) |
        Q(descricao__icontains = itemDaPesquisa) |
        Q(tipoDeItem__icontains = itemDaPesquisa) |
        Q(slug__icontains = itemDaPesquisa) |
        Q(categoria__nodeDaCategoria__icontains = itemDaPesquisa)
      )
    paginator = Paginator(listadelocais, 10) # Show 25 contacts per page.
    page = request.GET.get('page')
    listadelocais = paginator.get_page(page)

    template = 'local/listadelocais.html'
    context = {
      'listaDeLocais' : listadelocais , 
      'listaDeCategorias' : listadecategorias, 
      'categoria' : categoria, 
      'teste': g.city}
    return render(request , template, context )



class LocaisCriar(FormView):
        #model = Local
        form_class = AdForm
        #fields = ['nome', 'tipoDeItem', 'categoria', 'descricao', 'logo', 'telefone', 'whatsapp', 'facebook', 'instagram','site','endereco', 'numero', 'pais', 'estado', 'municipio', 'cep', ]
        #readonly_fields = ('responsavel')
        template_name = 'local/criarlocal.html'
        success_url = "/locais/criar/sucesso"


      

        def form_valid(self, form):
          self.object = form.save(commit=False)
          form.instance.responsavel = self.request.user
          self.object.save()
          return super().form_valid(form)







def carregarEstados(request):
      pais_id = request.GET.get('pais')
      estados = Estado.objects.all()

      template = 'local/dropdownEstado.html'
      context = {'estados': estados}
      return render(request , template, context)  

class LocalSucesso(TemplateView):
      template_name = 'local/sucessolocal.html'









# def detalhesdolocal(request, slugDoLocal):
#     detalhesdolocal = Local.objects.get(slug=slugDoLocal)
#     galeriadefotos = GaleriaDeFotos.objects.filter(local=detalhesdolocal)
#     promocoesDosLocais = Promocoes.objects.all().filter(local__id=detalhesdolocal.id)
#     template = 'local/detalhesdolocal.html'
#     context = {
#       'detalhesDoLocal' : detalhesdolocal , 
#       'GaleriaDeFotos' : galeriadefotos,
#       'listaDePromocoes': promocoesDosLocais

#       }
#     return render(request , template, context) 






class ListaDeCategoriasView(ListView):
    model = CategoriaDoLocal
    template_name = 'local/listadesubcategorias.html'
    query_pk_and_slug = True
    slug_field = 'slug'
    slug_url_kwarg = 'slugCatPai'
    pk_field = 'id'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        kwargs['categoriaPai'] = CategoriaDoLocal.objects.get(slug=self.kwargs['slugCatPai'])
        kwargs['listaDeSubCategorias'] = CategoriaDoLocal.objects.filter(categoriaBase__slug=self.kwargs['slugCatPai'])
        # kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)


class ListaDeLocaisPorCategoriaView(ListView):
    model = Local
    template_name = 'local/listadelocais.html'
    query_pk_and_slug = True
    slug_field = 'slug'
    slug_url_kwarg = 'slugCat'
    pk_field = 'id'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        kwargs['categoriaPai'] = CategoriaDoLocal.objects.get(slug=self.kwargs['slugCat'])
        kwargs['listaDeLocais'] = Local.objects.filter(categoria__slug=self.kwargs['slugCat'])
        # kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)





      