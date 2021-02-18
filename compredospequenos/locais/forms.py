from django import forms
from django_select2.forms import ModelSelect2Widget
from django.core.exceptions import ValidationError

from .models import Local, CategoriaDoLocal
from localidades.models import Pais, Estado, Municipio
from localidades.forms import PaisWidget,EstadoWidget,MunicipioWidget




class AdForm(forms.ModelForm):
    
    class Meta:
        model = Local
        fields = ['nome',  'categoria', 'descricao', 'logo', 'telefone', 'whatsapp', 'facebook', 'instagram','site','email',]
        readonly_fields = ('responsavel', 'criado')
        success_url = "/anuncios/criar/sucesso"


        labels = {
        'nome':'Nome do Negócio',
        'categoria':'Categoria',
        'descricao':'Descreva seu Negócio',
        'logo': 'Logotipo ou Foto do Negócio',
        'telefone': 'Telefone para Contato',
        'whatsapp': 'Whatsapp',
        'facebook': 'Facebook',
        'instagram': 'Instagram',
        'site': 'Site ou Página na Web',
        'email': 'Email',
        }

            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    def send_email(self):
            # send email using the self.cleaned_data dictionary
        pass



