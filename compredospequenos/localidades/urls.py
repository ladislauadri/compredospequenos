from django.urls import include, path
from . import views
from . import views_localidades

app_name = 'Municipios'

urlpatterns = [
    path('', views_localidades.listademunicipios, name='listaDeMunicipios'),

    


]