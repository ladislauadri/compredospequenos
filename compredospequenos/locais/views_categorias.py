from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count




from .models import (
  Local, 
  GaleriaDeFotosDosLocais, 
  CategoriaDoLocal)



def listadecategorias(request):
  listadecategorias = CategoriaDoLocal.objects.annotate(todasAsCategorias=Count('anuncio')).order_by('nodeDaCategoria')

  itemDaPesquisa = request.GET.get('busca')
  if itemDaPesquisa:
    listadecategorias = listadecategorias.filter(
      Q(nome__icontains = itemDaPesquisa) |
      Q(slug__icontains = itemDaPesquisa) 
    )


  template = 'anuncio/listadecategorias.html'
  context = {'listaDeCategorias' : listadecategorias ,}
  return render(request , template, context)
