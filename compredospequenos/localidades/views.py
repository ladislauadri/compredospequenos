from django.shortcuts import render
from .models import (
  Pais, 
  Estado, 
  Municipio)

def carregarEstados(request):
    pais_id = request.GET.get('pais')
    estados = Estado.objects.all().filter(pais_id=pais_id)
    return render(request, 'enxertos/dropdownEstado.html', {'estados': estados})