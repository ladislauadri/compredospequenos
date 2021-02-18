from django.urls import include, path
from . import views
from . import views_localidades

app_name = 'Estados'

urlpatterns = [
    path('', views_localidades.listadeestados, name='listaDeEstados'),
    path('<slug:slug>', views_localidades.detalhesdoestado, name='listaDeMunicipiosPorEstado'),


    


]