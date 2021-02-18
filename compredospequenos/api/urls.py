# Core Django Imports
from django.urls import path

# Blog application imports
from blog.api.v1.views.category_views import CategoryList
from blog.api.v1.views.article_views import ArticleList, CategoryArticleList
from posts.views import (
    PostAPIView,
    
)

app_name = 'api'


urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('articles/', ArticleList.as_view()),
    path('post/', PostAPIView.as_view({'get': 'list'})),
    # path('<str:category_name>/', CategoryArticleList.as_view()),
    # path('locais/', ListaDeLocais.as_view(), name='locais'),
    # path('catlocais/', ListaDeCategorias, name='categoriasdoslocais'),
]
