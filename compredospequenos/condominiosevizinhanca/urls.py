from django.contrib import admin
from django.urls import path, re_path ,include
from django.conf import settings
from django.conf.urls.static import static
from homepage import views
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from homepage.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView
from .views import SitemapXMLView, HomepageView, ArticleListView 

# from anuncios.models import Anuncio, CategoriaDoAnuncio
from localidades.models import Pais, Estado, Municipio
# from promocoes.models import Promocoes, CategoriaPromocional
from paginas.models import Pagina, CategoriaDasPaginas
from blog.views.blog.article_views import (
    ArticleListView,
    ArticleDetailView,
    ArticleSearchListView,
    TagArticlesListView,
)


app_name= "condominiosevizinhanca"
 
# negociosSitemaps = {
#     'blog': GenericSitemap({
#         'queryset': Anuncio.objects.all(),
#         'date_field': 'atualizado',
#     }, priority=0.9),
#     'static': StaticViewSitemap,
# }
 
urlpatterns = [
    # path('', homepage, name='home'),
    path('', HomepageView.as_view(), name='home'),
    path(
        route='@<str:username>/<str:slug>/',
        view=ArticleDetailView.as_view(),
        name='article_detail'

    ),
#     path('sitemap/negociositemap.xml', sitemap, {'sitemaps': negociosSitemaps },
#      name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('locais/', include('locais.urls', namespace='locais')),
    path('municipios/', include('localidades.urls', namespace='municipios')),
    path('estados/', include('localidades.urls_estados', namespace='estados')),
    path('contas/', include('contas.urls', namespace='contas')),
    path(
        route='artigos/',
        view=ArticleListView.as_view(),
        name='article_list'

    ),
    path('ocorrencias/', include('issueTracker.urls', namespace='ocorrencias')),
    # path('painel/', include('dashboard.urls', namespace='painel')),
    path('paginas/', include('paginas.urls', namespace='paginas')),
    path("select2/", include("django_select2.urls")),
    re_path(r'^taggit/', include('taggit_selectize.urls')),
    re_path(r'^chaining/', include('smart_selects.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^comments/', include('django_comments.urls')),
    path('api/v1/', include('api.urls', namespace='api'))
    



] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
