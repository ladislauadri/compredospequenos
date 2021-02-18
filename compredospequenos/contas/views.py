from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login




from .forms import UserForm

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password1']
             )
            login(request, new_user)
            return HttpResponseRedirect('/')

    else:
        user_form = UserForm()

    context = {'user_form' : user_form}

    return render(request , 'contas/registro.html' , context)
