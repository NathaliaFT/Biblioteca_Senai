from django.shortcuts import render

from biblioteca.forms import Newsletter

# Create your views here.


def index(request):
    form = Newsletter
    return render (request, 'index.html', {'form':form})

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




