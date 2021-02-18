from django.urls import path, re_path, include, reverse
from . import views
from .views import (
  LocaisCriar,
  LocalSucesso,
  DetalhesDoLocalView,
  ListaDeLocaisView,
  ListaDeCategoriasView,
  ListaDeLocaisPorCategoriaView
)
from .views_categorias import (
  listadecategorias,
)


app_name = 'locais'

urlpatterns = [
  # path('', views.listadelocais, name='listaDeLocais'),
  path('', ListaDeLocaisView.as_view(), name='listaDeLocais'),
  # path('<slug:slugDaCategoria>', views.listadelocais, name='listaDeLocaisPorCategoria'),
  path('c/<slugCatPai>', ListaDeCategoriasView.as_view(), name='listaDeSubCategoriasPorCategoria'),
  path('<slugCat>', ListaDeLocaisPorCategoriaView.as_view(), name='listaDeLocaisPorCategoria'),
  path('negocio/<slug:slug>', DetalhesDoLocalView.as_view(), name='detalhesDoLocal'),
  path('criar/', LocaisCriar.as_view(), name='CriarLocal'),
  path('categorias/', listadecategorias, name='Categorias'),
  path('criar/sucesso/', LocalSucesso.as_view(), name='LocalSucesso'),
  path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
  path("select2/", include("django_select2.urls")), 

 
]