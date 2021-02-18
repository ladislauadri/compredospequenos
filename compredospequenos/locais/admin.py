from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.auth.models import User
from django.conf import settings
from model_clone import CloneModelAdmin



from .models import (
  Local,
  CategoriaDoLocal,
  LocalEndereco,
  ContatoDoLocal,
  TipoDeLocal,
  GaleriaDeFotosDosLocais,
  Promocoes,
  CategoriaPromocional,
  BaseDePromocoes
)


admin.site.register(CategoriaDoLocal, admin.OSMGeoAdmin) 
admin.site.register(LocalEndereco, admin.OSMGeoAdmin) 
admin.site.register(ContatoDoLocal, admin.OSMGeoAdmin) 
admin.site.register(TipoDeLocal, admin.OSMGeoAdmin) 
admin.site.register(GaleriaDeFotosDosLocais, admin.OSMGeoAdmin) 




@admin.register(Local)
class PromocoesAdmin(CloneModelAdmin):
    list_display = (
        'nome',  
        'categoria',
        'descricao', 
        'logo', 
        'telefone', 
        'whatsapp',
        'facebook', 
        'instagram',
        'site',
        'email',)

    readonly_fields=['id', 'slug']
 
    list_filter = (
        'nome',  
        'categoria',
        'descricao', 
        'logo', 
        'telefone', 
        'whatsapp',
        'facebook', 
        'instagram',
        'site',
        'email', )
    search_fields = (
        'nome',  
        'categoria',
        'descricao', 
        'logo', 
        'telefone', 
        'whatsapp',
        'facebook', 
        'instagram',
        'site',
        'email',)
    actions = ['CriadosPor']
    
    def CriadosPor(self, request, queryset):
        return queryset.annotate(local__responsavel__contains=self.request.user) 


@admin.register(Promocoes)
class PromocoesAdmin(CloneModelAdmin):
    list_display = (
        'id', 
        'nome', 
        'prazoDaOferta',
        'local', 
        'info', 
        'linkDeCompra', 
        'precoReal', 
        'precoPromocional', 
        'fotoDoLocal',
        'createdAt',
        'updatedAt',
        'slug'
        )
    readonly_fields=['id', 'slug']
 
    list_filter = ('nome', 'local', 'categorias', 'updatedAt')
    search_fields = (
        'nome', 
        'prazoDaOferta',
        'local', 
        'info', 
        'linkDeCompra', 
        'precoReal', 
        'precoPromocional', 
        'fotoDoLocal',
        'createdAt',
        'updatedAt'
        )
    actions = ['CriadosPor']
    
    def CriadosPor(self, request, queryset):
        return queryset.annotate(local__responsavel__contains=self.request.user) 


@admin.register(CategoriaPromocional)
class CategoriaPromocionalAdmin(admin.ModelAdmin):
    pass
