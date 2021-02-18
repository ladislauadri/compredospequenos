from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
import requests
import json
import urllib

from ipware import get_client_ip

from locais.models import Local, CategoriaDoLocal
from localidades.models import Pais, Estado, Municipio
# from promocoes.models import Promocoes, CategoriaPromocional
from paginas.models import Pagina, CategoriaDasPaginas
from blog.models.article_models import Article
from blog.models.category_models import Category
from blog.forms.blog.comment_forms import CommentForm
from taggit.models import Tag


class HomepageView(ListView):
    model = Local
    template_name = 'homepage/home_condo.html'
    

    def get_context_data(self, **kwargs):
      # client_ip, is_routable = get_client_ip(self.request)
      # api_key = '85333f4c26c48b675004450cdf8575d1'
      # q = client_ip
      # URL = "http://api.ipstack.com/{}?access_key={}&format=1".format(q, api_key)
      # response = urllib.request.urlopen(URL)
      # data = json.loads(response.read())


      
      context = super().get_context_data(**kwargs)
      context['listaDeLocais'] = Local.objects.all().filter(ativo=True)[:5]
      context['listaDeArtigos'] = Article.objects.all().filter(sites__id=4)[:10]
      # context['url'] = data
      # context['paginas'] = Pagina.objects.filter(ativo=True)
      return context
    

class SitemapXMLView(TemplateView):
  # template_name = 'sitemap/sitemapxml.html'
  content_type = 'application/xml'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['artigos'] = ArtigosBlog.objects.filter(status=1)
      context['locais'] = Local.objects.filter(ativo=True)
      context['paginas'] = Pagina.objects.filter(ativo=True)
      return context


class ArticleListView(ListView):
    context_object_name = "articles"
    paginate_by = 10
    queryset = Article.objects.filter(sites__id=4).filter(status=Article.PUBLISHED, deleted=False)
    template_name = "blog/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article/article_detail.html'

    def get_context_data(self, **kwargs):
        session_key = f"viewed_article {self.object.slug}"
        if not self.request.session.get(session_key, False):
            self.object.views += 1
            self.object.save()
            self.request.session[session_key] = True
        


        kwargs['related_articles'] = self.object.tags.similar_objects()[:4]
        kwargs['article'] = self.object
        kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)


class ArticleSearchListView(ListView):
    model = Article
    paginate_by = 12
    context_object_name = 'search_results'
    template_name = "blog/article/article_search_list.html"

    def get_queryset(self):
        """
        Search for a user input in the search bar.

        It pass in the query value to the search view using the 'q' parameter.
        Then in the view, It searches the 'title', 'slug', 'body' and fields.

        To make the search a little smarter, say someone searches for
        'container docker ansible' and It want to search the records where all
        3 words appear in the article content in any order, It split the query
        into separate words and chain them.
        """

        query = self.request.GET.get('q')

        if query:
            query_list = query.split()
            search_results = Article.objects.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(slug__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(body__icontains=q) for q in query_list))
            )

            if not search_results:
                messages.info(self.request, f"No results for '{query}'")
                return search_results.filter(status=Article.PUBLISHED, deleted=False)
            else:
                messages.success(self.request, f"Results for '{query}'")
                return search_results.filter(status=Article.PUBLISHED, deleted=False)
        else:
            messages.error(self.request, f"Sorry you did not enter any keyword")
            return []

    def get_context_data(self, **kwargs):
        """
            Add categories to context data
        """
        context = super(ArticleSearchListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        return context


class TagArticlesListView(ListView):
    """
        List articles related to a tag.
    """
    model = Article
    paginate_by = 12
    context_object_name = 'tag_articles_list'
    template_name = 'blog/article/tag_articles_list.html'

    def get_queryset(self):
        """
            Filter Articles by tag_name
        """

        tag_name = self.kwargs.get('tag_name', '')

        if tag_name:
            tag_articles_list = Article.objects.filter(tags__name__in=[tag_name],
                                                       status=Article.PUBLISHED,
                                                       deleted=False
                                                       )

            if not tag_articles_list:
                messages.info(self.request, f"No Results for '{tag_name}' tag")
                return tag_articles_list
            else:
                messages.success(self.request, f"Results for '{tag_name}' tag")
                return tag_articles_list
        else:
            messages.error(self.request, "Invalid tag")
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        return context
