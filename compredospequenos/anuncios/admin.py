from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin



from .models import Anuncio, CategoriaDoAnuncio, GaleriaDeFotos


admin.site.register(Anuncio, admin.OSMGeoAdmin) 
admin.site.register(CategoriaDoAnuncio, admin.OSMGeoAdmin) 
admin.site.register(GaleriaDeFotos, admin.OSMGeoAdmin) 

