  from django.shortcuts import render, redirect
  from .models import (
    Anuncio, 
    GaleriaDeFotos, 
    CategoriaDoAnuncio)
  from promocoes.models import (
    Promocoes, 
    CategoriaPromocional
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






  def listadeanuncios(request, slugDaCategoria=None):
    categoria = None
    listadeanuncios = Anuncio.objects.all().filter(ativo=True).order_by('-criado')
    listadecategorias = CategoriaDoAnuncio.objects.annotate(todasAsCategorias=Count('anuncio'))
    teste = request.META['HTTP_X_FORWARDED_FOR'] 
    g = geocoder.ipinfo(teste)



    if slugDaCategoria :
      categoria = CategoriaDoAnuncio.objects.get(slug=slugDaCategoria)
      listadeanuncios = listadeanuncios.filter(categoria=categoria)

    itemDaPesquisa = request.GET.get('busca')
    if itemDaPesquisa:
      listadeanuncios = listadeanuncios.filter(
        Q(nome__icontains = itemDaPesquisa) |
        Q(descricao__icontains = itemDaPesquisa) |
        Q(tipoDeItem__icontains = itemDaPesquisa) |
        Q(slug__icontains = itemDaPesquisa) |
        Q(categoria__nodeDaCategoria__icontains = itemDaPesquisa)
      )
    paginator = Paginator(listadeanuncios, 10) # Show 25 contacts per page.
    page = request.GET.get('page')
    listadeanuncios = paginator.get_page(page)

  

    template = 'anuncio/listadeanuncios.html'
    context = {
      'listaDeAnuncios' : listadeanuncios , 
      'listaDeCategorias' : listadecategorias, 
      'categoria' : categoria, 
      'teste': g.city,
      }
    return render(request , template, context )




  def listadeanuncios2(request, slugDaCategoria=None):
    teste = request.META['HTTP_X_FORWARDED_FOR'] 
    g = geocoder.ipinfo(teste)
    categoria = None
    listadeanuncios = Anuncio.objects.all().filter( municipio__nome__contains=g.city )
    listadecategorias = CategoriaDoAnuncio.objects.annotate(todasAsCategorias=Count('anuncio'))





    if slugDaCategoria :
      categoria = CategoriaDoAnuncio.objects.get(slug=slugDaCategoria)
      listadeanuncios = listadeanuncios.filter(categoria=categoria)

    itemDaPesquisa = request.GET.get('busca')
    if itemDaPesquisa:
      listadeanuncios = listadeanuncios.filter(
        Q(nome__icontains = itemDaPesquisa) |
        Q(descricao__icontains = itemDaPesquisa) |
        Q(tipoDeItem__icontains = itemDaPesquisa) |
        Q(slug__icontains = itemDaPesquisa) |
        Q(categoria__nodeDaCategoria__icontains = itemDaPesquisa)
      )
    paginator = Paginator(listadeanuncios, 10) # Show 25 contacts per page.
    page = request.GET.get('page')
    listadeanuncios = paginator.get_page(page)

    template = 'anuncio/listadeanuncios.html'
    context = {
      'listaDeAnuncios' : listadeanuncios , 
      'listaDeCategorias' : listadecategorias, 
      'categoria' : categoria, 
      'teste': g.city}
    return render(request , template, context )



  class AnunciosCriar(FormView):
        #model = Anuncio
        form_class = AdForm
        #fields = ['nome', 'tipoDeItem', 'categoria', 'descricao', 'logo', 'telefone', 'whatsapp', 'facebook', 'instagram','site','endereco', 'numero', 'pais', 'estado', 'municipio', 'cep', ]
        #readonly_fields = ('responsavel')
        template_name = 'anuncio/criaranuncio.html'
        success_url = "/anuncios/criar/sucesso"


      

        def form_valid(self, form):
          self.object = form.save(commit=False)
          form.instance.responsavel = self.request.user
          self.object.save()
          return super().form_valid(form)







  def carregarEstados(request):
      pais_id = request.GET.get('pais')
      estados = Estado.objects.all()

      template = 'anuncio/dropdownEstado.html'
      context = {'estados': estados}
      return render(request , template, context)  

  class AnuncioSucesso(TemplateView):
      template_name = 'anuncio/sucessoanuncio.html'




      



  def detalhesdoanuncio(request, slugDoAnuncio):
    detalhesdoanuncio = Anuncio.objects.get(slug=slugDoAnuncio)
    galeriadefotos = GaleriaDeFotos.objects.filter(anuncio=detalhesdoanuncio)
    promocoesDosAnuncios = Promocoes.objects.all().filter(anuncio__id=detalhesdoanuncio.id)
    template = 'anuncio/detalhesdoanuncio.html'
    context = {
      'detalhesDoAnuncio' : detalhesdoanuncio , 
      'GaleriaDeFotos' : galeriadefotos,
      'listaDePromocoes': promocoesDosAnuncios

      }
    return render(request , template, context) 





      