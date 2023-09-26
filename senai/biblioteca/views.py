from django.shortcuts import render

# Create your views here.


def index(request):
    return render (request, 'index.html');

def infantil(request):
    return render (request, 'infantil.html')

def romance(request):
    return render (request, 'romance.html')

def Fic(request):
    return render (request, 'Fic.html')

def Fantasia(request):
    return render (request, 'Fantasia.html')

def carrinho(request):
    return render (request, 'carrinho.html')


