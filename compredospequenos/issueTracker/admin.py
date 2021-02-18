# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models.ocorrenciaModelo import Ocorrencia
from .models.ocorrenciaCategoriaModelo import OcorrenciaCategoria
from .models.ocorrenciaFotosModelo import OcorrenciaFotos
from blog.models.comment_models import Comment
from blog.models.author_models import Profile



class OcorrenciaCategoriaAdmin(admin.ModelAdmin):

    list_display = ('nome', 'slug', 'dataCriacao', 'aprovada')
    list_filter = ('nome', 'aprovada',)
    search_fields = ('nome', 'aprovada',)
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['-nome', ]


# Registers the category model at the admin backend.
admin.site.register(OcorrenciaCategoria, OcorrenciaCategoriaAdmin)


class OcorrenciaAdmin(admin.ModelAdmin):

    # list_display = ('categoria', 'titulo', 'slug', 'reclamante', 'descrição', 'endereco',
    #                 'numero', 'complemento', 'municipio', 'estado', 'pais', 'cep', 'poder', 'estadoDaOcorrencia', 'anonimo', 'deletado')
    list_display = ('categoria', 'titulo', 'slug', 'reclamante', 'descrição', 'endereco',
                    'numero', 'complemento', 'cep', 'poder', 'estadoDaOcorrencia', 'anonimo', 'deletado')
    list_filter = ('categoria', 'cep', 'estadoDaOcorrencia', 'poder',)
    search_fields = ('titulo', 'descrição', 'endereco',)
    raw_id_fields = ('reclamante',)
    date_hierarchy = 'dataCriacao'
    ordering = ['-dataAtualizacao', '-dataCriacao', ]
    # readonly_fields = ('')


# Registers the article model at the admin backend.
admin.site.register(Ocorrencia, OcorrenciaAdmin)


class OcorrenciaFotosAdmin(admin.ModelAdmin):

    list_display = ('ocorrencia',)
    list_filter = ('ocorrencia',)
    search_fields = ('ocorrencia',)
    date_hierarchy = 'dataCriacao'
    ordering = ['-dataCriacao', ]


# Registers the comment model at the admin backend.
admin.site.register(OcorrenciaFotos, OcorrenciaFotosAdmin)
