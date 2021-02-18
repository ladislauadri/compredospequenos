from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This already exists!'})
    username = forms.CharField(required=True, label='Nome do usuário', min_length=4, max_length=150)
    password1 = forms.CharField(required=True, label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Confirme sua senha', widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.Textarea, min_length=10, label="Fale um pouco sobre você")
    accept_terms = forms.BooleanField(required=True , label='Aceito os Termos & Condições')
    


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("O nome de Usuário já está em uso")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("O email já está em uso")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("As Senhas precisam ser iguais!")
 
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        return user

