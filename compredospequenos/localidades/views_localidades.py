from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count


from .models import (
  Pais,
  Estado,
  Municipio,
)

# from anuncios.models import (
#   Anuncio, 
#   GaleriaDeFotos, 
#   CategoriaDoAnuncio)



def listademunicipios(request):
  listademunicipios = Municipio.objects.all().order_by('nome')

  itemDaPesquisa = request.GET.get('busca')
  if itemDaPesquisa:
    listademunicipios = listademunicipios.filter(
      Q(nome__icontains = itemDaPesquisa) |
      Q(slug__icontains = itemDaPesquisa) 
    )


  template = 'anuncio/listademunicipios.html'
  context = {'listaDeMunicipios' : listademunicipios ,}
  return render(request , template, context)


def detalhesdomunicipio(request, slugDoMunicipio):
      detalhesdomunicipio = Municipio.objects.get(slug=slugDoMunicipio)
      galeriadefotos = GaleriaDeFotos.objects.filter(municipio=detalhesdomunicipio)
      template = 'anuncio/detalhesdomunicipio.html'
      context = {'detalhesDoMunicipio' : detalhesdomunicipio , 'GaleriaDeFotos' : galeriadefotos}
      return render(request , template, context) 



def listadeestados(request):
  listadeestados = Estado.objects.filter(pais__nome__contains='Brasil').order_by('nome')
  listadeanuncios = Anuncio.objects.all().filter(pais__nome__contains='Brasil')


  itemDaPesquisa = request.GET.get('busca')
  if itemDaPesquisa:
    listadeestados = listadeestados.filter(
      Q(nome__icontains = itemDaPesquisa) |
      Q(slug__icontains = itemDaPesquisa) |
      Q(municipio__icontains = itemDaPesquisa) 
    )


  template = 'anuncio/listadeestados.html'
  context = {
    'listaDeEstados' : listadeestados ,
    'listaDeAnuncios' : listadeanuncios ,
    }
  return render(request , template, context)


def detalhesdoestado(request, slug):
      detalhesdoestado = Estado.objects.get(slug=slug)
      detalhesdomunicipio = Municipio.objects.filter( estado__slug__contains=slug )
      listadeanuncios = Anuncio.objects.all().filter( estado__slug__contains=slug )


      template = 'anuncio/detalhesdoestado.html'
      context = {
        'detalhesDoEstado' : detalhesdoestado , 
        'listaDeMunicipios' : detalhesdomunicipio,
        'listaDeAnuncios' : listadeanuncios , 
        }
      return render(request , template, context) 
