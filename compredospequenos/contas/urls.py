from django.urls import path, re_path
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from . views import register


app_name = 'contas'

urlpatterns = [
  path('entrar/', auth_views.LoginView.as_view(template_name='contas/entrar.html'), name='login'),
  path('esqueci-a-senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  path('sair/', auth_views.LogoutView.as_view(template_name='contas/sair.html'), name='logout'),
  path('registro/' , register , name='register') , 


]