from django import forms
from django_select2.forms import ModelSelect2Widget
from django.core.exceptions import ValidationError

from issueTracker.models.ocorrenciaModelo import Ocorrencia




class OcorrenciaForm(forms.ModelForm):
    
    class Meta:
        model = Ocorrencia
        # fields = ['titulo','categoria','descrição','endereco', 'numero', 'complemento', 'pais', 'estado', 'municipio', 'cep', 'poder',]
        fields = ['titulo','categoria','descrição','endereco', 'numero', 'complemento',  'cep', 'poder',]
        # fields_required = ['titulo','categoria','descrição','endereco', 'numero', 'pais', 'estado', 'municipio', ]
        fields_required = ['titulo','categoria','descrição','endereco', 'numero',  ]
        #  = ['cep']
        # readonly_fields = ('responsavel', 'criado')
        # success_url = "/anuncios/criar/sucesso"


    #     labels = {
    #     'nome':'Nome do Negócio',
    #     'categoria':'Categoria',
    #     'descricao':'Descreva seu Negócio',
    #     'logo': 'Logotipo ou Foto do Negócio',
    #     'telefone': 'Telefone para Contato',
    #     'whatsapp': 'Whatsapp',
    #     'facebook': 'Facebook',
    #     'instagram': 'Instagram',
    #     'site': 'Site ou Página na Web',
    #     'endereco': 'Endereço',
    #     'numero': 'Número',
    #     'complemento': 'Complemento',
    #     'pais': 'País',
    #     'estado': 'Estado',
    #     'municipio':'Municipio',
    #     'cep':'CEP',
    #     }

            
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cep'].required



    # def send_email(self):
    #         # send email using the self.cleaned_data dictionary
    #     pass



