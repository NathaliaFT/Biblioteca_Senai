from django.shortcuts import render, redirect
from .models import *
from biblioteca.forms import *
from django.contrib import messages

# Create your views here.


def index(request):
    form = Newsletter()
    login_form= Login()
    return render (request, 'index.html', {
    'form':form,
    'login_form': login_form})

def infantil(request):
    x = Newsletter()
    return render (request, 'infantil.html', {
        'form':x
    })

def romance(request):
    return render (request, 'romance.html')

def Fic(request):
    return render (request, 'Fic.html')

def Fantasia(request):
    return render (request, 'Fantasia.html')

def carrinho(request):
    return render (request, 'carrinho.html')

def login(request):
    return render (request, 'login.html')
    if request.method == "POST":
        form = Login(request.POST)

        if form.is_valid():
            email =form['email'].value()
            password = form['password'].value()
            messages.sucess(request, f'{email} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, f'{email} erro ao realizar o login!')
            return redirect('index')


def nov(request):
    if request.method =="POST":
        bd = Categoria(nome=request.POST['email_news'])
        bd.save()
        messages.success(request, f'email cadastrado com sucessos!')
        return redirect('index')

def delete(request, id):
    x = Categoria.objects.get(pk=id)
    x.delete()
    messages.error(request, f'email deletado com sucesso!')
    return redirect('index')



