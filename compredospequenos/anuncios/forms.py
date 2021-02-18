from django import forms
from django_select2.forms import ModelSelect2Widget
from django.core.exceptions import ValidationError

from .models import Anuncio, CategoriaDoAnuncio
from localidades.models import Pais, Estado, Municipio
from localidades.forms import PaisWidget,EstadoWidget,MunicipioWidget




class AdForm(forms.ModelForm):
    
    class Meta:
        model = Anuncio
        fields = ['nomeDoAnuncio', 'tipoDeAnuncio', 'categoriaDoAnuncio', 'descricao', 'logo', 'telefone', 'whatsapp', 'facebook', 'instagram','site','endereco', 'numero', 'complemento','pais', 'estado', 'municipio', 'cep', ]
        fields_required = ['cep']
        readonly_fields = ('responsavel', 'criado')
        success_url = "/anuncios/criar/sucesso"


        labels = {
        'nomeDoAnuncio':'Nome do Negócio',
        'tipoDeAnuncio':'Tipo de Negócio',
        'categoriaDoAnuncio':'Categoria',
        'descricao':'Descreva seu Negócio',
        'logo': 'Logotipo ou Foto do Negócio',
        'telefone': 'Telefone para Contato',
        'whatsapp': 'Whatsapp',
        'facebook': 'Facebook',
        'instagram': 'Instagram',
        'site': 'Site ou Página na Web',
        'endereco': 'Endereço',
        'numero': 'Número',
        'complemento': 'Complemento',
        'pais': 'País',
        'estado': 'Estado',
        'municipio':'Municipio',
        'cep':'CEP',
        }

            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cep'].required



    def send_email(self):
            # send email using the self.cleaned_data dictionary
        pass



