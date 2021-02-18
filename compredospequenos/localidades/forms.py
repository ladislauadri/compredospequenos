from django import forms
from django_select2 import forms as s2forms
from .models import Pais, Estado, Municipio

class PaisWidget(s2forms.ModelSelect2Widget):
    model=Pais,
    search_fields = ["nome__icontains",]
class EstadoWidget(s2forms.ModelSelect2Widget):
    model=Estado,
    search_fields=['nome__icontains'],
    dependent_fields={'pais': 'pais'},
class MunicipioWidget(s2forms.ModelSelect2Widget):
    model=Municipio,
    search_fields=['nome__icontains'],
    dependent_fields={'estado': 'estado'},



class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ('nome', 'pais',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['municipio'].queryset = Municipio.objects.none()


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()