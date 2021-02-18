from django.urls import path, re_path, include, reverse
from . import views
# from anuncios.views import (
#   AnunciosCriar,
#   AnuncioSucesso,
# )
from .views import (
  HomepageDash,
#   ListaDeAnunciosDash,
#   ListaDePromocoesDash,
#   DetalhesDaPromocoesDash,
#   DetalhesDoAnuncioDash,
#   AtualizarAnuncioDash,
#   AtualizarPromocoesDash,
#   DeletarAnuncioDash,
#   DeletarPromocoesDash,
#   CriarAnunciosDash,
#   CriarPromocoesDash,
)
# from anuncios.views_categorias import (
#   listadecategorias,
# )
from django.conf import settings
from django.conf.urls.static import static

app_name = 'painel'

urlpatterns = [
  path('', HomepageDash.as_view(), name='HomePageDashDash'),
  # path('anuncios/', ListaDeAnunciosDash.as_view(), name='listaDeAnunciosDash'),
  # path('anuncios/criar/', CriarAnunciosDash.as_view(), name='CriarAnunciosDash'),
  # path('anuncios/<slug:slug>/', DetalhesDoAnuncioDash.as_view(), name='DetalhesDoAnuncioDash'),
  # path('anuncios/<slug:slug>/atualizar/', AtualizarAnuncioDash.as_view(), name='AtualizarAnuncioDash'),
  # path('anuncios/<slug:slug>/excluir/', DeletarAnuncioDash.as_view(), name='DeletarAnuncioDash'),
  
  # path('promocoes/', ListaDePromocoesDash.as_view(), name='listaDePromocoesDash'),
  # path('promocoes/criar/', CriarPromocoesDash.as_view(), name='CriarPromocoesDash'),
  # path('promocoes/<slug:slug>/', DetalhesDaPromocoesDash.as_view(), name='DetalhesDaPromocoesDash'),
  # path('promocoes/<slug:slug>/atualizar/', AtualizarPromocoesDash.as_view(), name='AtualizarPromocoesDash'),
  # path('promocoes/<slug:slug>/excluir/', DeletarPromocoesDash.as_view(), name='DeletarPromocoesDash'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
