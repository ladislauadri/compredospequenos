import csv
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect, render



from .models import Pais, Estado, Municipio
from .forms import CsvImportForm

class LocalidadesAdmin(admin.ModelAdmin):
    pass

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    pass

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    pass

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_filter = ['estado']
    search_fields = ('estado', 'nome')
    actions = ['slug']

