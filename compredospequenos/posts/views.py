from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import viewsets


from .models import Post
from .serializers import PostSerializer

from queryset_sequence import QuerySetSequence

from locais.models import Local, CategoriaDoLocal
from localidades.models import Pais, Estado, Municipio
# from promocoes.models import Promocoes, CategoriaPromocional
from paginas.models import Pagina, CategoriaDasPaginas
from posts.models import Post
from blog.models.article_models import Article




# Third-party apps import

# Blog app imports

class PostView(ListView):
    
    model = Post
    paginate_by = 100  # if pagination is desired
    context_object_name = 'tipoDeLocal'
    template_name = 'local/listadelocais.html'

    def get_context_data(self, **kwargs):
        kwargs['listaDeLocais'] = Post.objects.all().order_by('-dataCriacao')
        # kwargs['estabelecimentos'] = LocalEndereco.objects.filter(local__pk=self.pk)
        # kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)

class DetalhesDoPostView(DetailView):
    model = Post
    template_name = 'local/detalhesdolocal.html'
    query_pk_and_slug = True
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        # kwargs['related_articles'] = self.object.tags.similar_objects()[:4]
        kwargs['detalhesDoLocal'] = self.object
        # kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)



class PostAPIView(viewsets.ModelViewSet):
    queryset = QuerySetSequence(Local.objects.all(), Post.objects.all(), Article.objects.all()).order_by('-createdAt')
    serializer_class  = PostSerializer(queryset, many=True) 

    def get_queryset(self):
        # This will return all Books first, then all Articles. Each of those
        # is individually ordered by ``author``, then ``title``.
        return QuerySetSequence(Local.objects.all(), Post.objects.all(), Article.objects.all()).order_by('-createdAt')