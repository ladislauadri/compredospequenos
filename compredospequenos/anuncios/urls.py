from django.urls import path, re_path, include, reverse
from . import views
from .views import (
  AnunciosCriar,
  AnuncioSucesso,
)
from .views_categorias import (
  listadecategorias,
)


app_name = 'anuncio'

urlpatterns = [
  path('', views.listadeanuncios, name='listaDeAnuncios'),
  path('<slug:slugDaCategoria>', views.listadeanuncios, name='listaDeAnunciosPorCategoria'),
  path('negocio/<slug:slugDoAnuncio>', views.detalhesdoanuncio, name='detalhesDoAnuncio'),
  path('criar/', AnunciosCriar.as_view(), name='CriarAnuncio'),
  path('categorias/', listadecategorias, name='Categorias'),
  path('criar/sucesso/', AnuncioSucesso.as_view(), name='AnuncioSucesso'),
  path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
  path("select2/", include("django_select2.urls")), 

 
]