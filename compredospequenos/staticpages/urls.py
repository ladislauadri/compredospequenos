from django.urls import path, re_path, include
from . import views
from django.views.generic import TemplateView

app_name = 'teste'


urlpatterns = [
    path('termos-e-condicoes', TemplateView.as_view(template_name='paginas/termos.html')),


]