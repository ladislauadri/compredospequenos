from django.shortcuts import render, get_object_or_404, redirect


from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from anuncios.models import Anuncio, GaleriaDeFotos, CategoriaDoAnuncio
# from promocoes.models import Promocoes
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
user = get_user_model()
from django.utils import timezone
from django.urls import reverse, reverse_lazy
# from .forms import AnunciosForm, PromocoesForm
from django.http import Http404





class HomepageDash(ListView):
    model = Anuncio
    template_name = 'crud/homepage.html'
    context_object_name = 'listaDeAnuncios'
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, self.request.path))
        else:
            return Anuncio.objects.filter(responsavel=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.order_by('nodeDaCategoria')
        return context

        
 

class ListaDeAnunciosDash(ListView): 
    model = Anuncio
    template_name = 'crud/listadeanunciosdash.html'
    context_object_name = 'anuncios'
    paginate_by = 10
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, self.request.path))
        return Anuncio.objects.filter(responsavel=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(ListaDeAnunciosDash, self).get_context_data(**kwargs)
        anuncios = self.get_queryset()
        page = self.request.GET.get('page')
        context['anuncios'] = anuncios
        return context

class DetalhesDoAnuncioDash(DetailView): 
    model = Anuncio
    template_name = 'crud/detalhesdeanunciosdash.html'
    context_object_name = 'anuncio'
    queryset = Anuncio.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

class CriarAnunciosDash(CreateView): 
    #model = Anuncio
    template_name = 'crud/criaranunciosdash.html'
    form_class = AnunciosForm
    success_url = reverse_lazy('painel:listaDeAnunciosDash')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.responsavel = self.request.user
        self.object.save()
        return super().form_valid(form)

class AtualizarAnuncioDash(UpdateView): 
    model = Anuncio
    form_class = AnunciosForm
    template_name = 'crud/atualizaranunciosdash.html'
    success_url = reverse_lazy('painel:listaDeAnunciosDash')


    @login_required
    def novoAnuncio(self, request):
        if request.method == 'POST':
            form = AnunciosForm(request.user, request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return redirect('products_list')
        else:
            form = AnunciosForm(request.user)
        return render(request, 'crud/atualizaranunciosdash.html', {'form': form})

class DeletarAnuncioDash(DeleteView): 
    model = Anuncio
    template_name = 'crud/excluiranunciosdash.html'

    success_url = reverse_lazy('painel:listaDeAnunciosDash')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeletarAnuncioDash, self).get_object()
        if not obj.responsavel == self.request.user:
            raise Http404
        return obj



class ListaDePromocoesDash(ListView, user): 
    model = Promocoes
    template_name = 'crud/listadepromocoesdash.html'
    context_object_name = 'promocoes'
    paginate_by = 10
    user = User
    @login_required
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Promocoes.objects.all()
        else:
            anunciosFiltrados = Anuncio.objects.all().filter(responsavel=self.request.user)
            return Promocoes.objects.all().filter(anuncio__responsavel=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(ListaDePromocoesDash, self).get_context_data(**kwargs)
        promocoes = self.get_queryset()
        page = self.request.GET.get('page')
        context['promocoes'] = promocoes
        return context

class DetalhesDaPromocoesDash(DetailView): 
    model = Promocoes
    template_name = 'crud/detalhesdepromocoesdash.html'
    context_object_name = 'promocao'
    queryset = Promocoes.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj



class CriarPromocoesDash(CreateView): 
    #model = Promocoes
    template_name = 'crud/criarpromocoesdash.html'
    form_class = PromocoesForm
    success_url = reverse_lazy('painel:listaDePromocoesDash')




class AtualizarPromocoesDash(UpdateView, user): 
    model = Promocoes
    form_class = PromocoesForm
    template_name = 'crud/atualizarpromocoesdash.html'
    success_url = reverse_lazy('painel:listaDePromocoesDash')


    @login_required
    def novaPromocao(self, request):
        if request.method == 'POST':
            form = PromocoesForm(request.user, request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return redirect('products_list')
        else:
            form = PromocoesForm(request.user)
        return render(request, 'crud/atualizarpromocoesdash.html', {'form': form})

class DeletarPromocoesDash(DeleteView): 
    model = Promocoes
    template_name = 'crud/excluirpromocoesdash.html'

    success_url = reverse_lazy('painel:listaDePromocoesDash')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeletarPromocoesDash, self).get_object()
        if not obj.anuncio.responsavel == self.request.user:
            raise Http404
        return obj