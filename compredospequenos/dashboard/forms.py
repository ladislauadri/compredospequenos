from django import forms
from django.forms import (
    ModelForm, 
    TextInput, 
    Textarea, 
    URLInput,
    ClearableFileInput,
    DateInput,
    SelectMultiple,
    Select,

    )
from promocoes.models import Promocoes
from anuncios.models import Anuncio
from ckeditor.widgets import CKEditorWidget
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.models import Permission, User
from django.db.models import Q
from django.contrib.auth.models import User
from crum import get_current_user

            


class AnunciosForm(ModelForm ):
    def __init__(self, *args, **kwargs):
        super(AnunciosForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.fields['cep'].required

    class Meta:
        model = Anuncio
        fields = [
            'nomeDoAnuncio', 
            'tipoDeAnuncio', 
            'categoriaDoAnuncio', 
            'descricao', 
            'logo', 
            'telefone', 
            'whatsapp', 
            'facebook', 
            'instagram',
            'site',
            'endereco', 
            'numero', 
            'complemento',
            'pais', 
            'estado', 
            'municipio', 
            'cep', 
        ]

        labels = {
        'nome':'Nome do Negócio',
        'tipoDeItem':'Tipo de Negócio',
        'categoria':'Categoria',
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


        fields_required = ['cep']
        readonly_fields = ('responsavel', 'criado')




class PromocoesForm(ModelForm ):
    def __init__(self, *args, **kwargs):
        super(PromocoesForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.fields['anuncio'].queryset = Anuncio.objects.filter(responsavel=user)
    prazoDaOferta = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y')
    )
    class Meta:
        model = Promocoes
        fields = (   
        'id',
        'nomeDaOferta',
        'categorias',
        'anuncio',
        'linkDeCompra',
        'info',
        'fotoDoAnuncio',
        'precoReal',
        'precoPromocional',
        'prazoDaOferta',
        
        )

        labels = {
        'nomeDaOferta':'Nome da oferta',
        'categorias':'Categorias',
        'anuncio':'A qual negócio a oferta pertence',
        'linkDeCompra':'Link para obter a oferta',
        'info':'Informações acerca da oferta',
        'fotoDoAnuncio':'Imagem da promoção',
        'precoReal':'Preço original',
        'precoPromocional':'Preço com desconto',
        'prazoDaOferta':'A promoção vai até?',
        }


    widgets ={

            }