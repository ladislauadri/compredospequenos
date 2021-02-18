from django.urls import path, re_path, include, reverse
from . import views
from .views import (
  DetalhesDaPagina,
  ListaDePagina,
)




app_name = 'paginas'

urlpatterns = [
  path('', ListaDePagina.as_view(), name='ListaDePagina'),
  path('<slug:slug>/', DetalhesDaPagina.as_view(), name='DetalhesDaPagina'),
  re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

 
]