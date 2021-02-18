from django.contrib import admin

from .models import Pagina, CategoriaDasPaginas
from django.contrib.auth.models import User
from django.conf import settings
from model_clone import CloneModelAdmin


@admin.register(Pagina)
class PaginaAdmin(CloneModelAdmin):
    pass

@admin.register(CategoriaDasPaginas)
class CategoriaDasPaginasAdmin(CloneModelAdmin):
    pass