from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

# from anuncios.models import Anuncio, CategoriaDoAnuncio
from localidades.models import Pais, Estado, Municipio
# from promocoes.models import Promocoes, CategoriaPromocional
from paginas.models import Pagina, CategoriaDasPaginas


class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # anuncio = Anuncio.objects.filter(ativo=True)
        pagina = Pagina.objects.filter(ativo=True)
        return ['anuncio:listaDeAnuncios']
    def location(self, item):
        return reverse(item)
