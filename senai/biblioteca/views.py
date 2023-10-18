from django.shortcuts import render, redirect
from .models import Usuario, Tarefa
from .forms import Newsletter
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import LoginForms

def index(request):
    form = Newsletter()
    login_form = LoginForms()
    return render(request, 'index.html', {
        'form': form,
        'login_form': login_form
    })

def admin(request):
    return render(request, "admin.html")

def crud(request):
    usuario = Usuario.objects.all()
    return render(request, "crud.html", {'usuarios':usuario})

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

def forms(request):
    return render (request, 'forms.html')


def nov(request):
    if request.method == "POST":
        bd = Categoria(nome=request.POST['email_news'])
        bd.save()
        messages.success(request, f'email cadastrado com sucessos!')
        return redirect('index')

def home(request):
    usuario = Usuario.objects.all()
    return render(request, "crud.html", {"usuario":usuario})
    

def create(request):
    Usuario.objects.create(
        nome=request.POST['nome'],
        cpf=request.POST['cpf'],
        email=request.POST['email'],
        senha=request.POST['senha'],
    )
    usuarios = Usuario.objects.all()
    return redirect('crud')

def edit(request, id):
    usuario = Usuario.objects.get(pk=id)
    return render(request, "editar.html", {'usuario':usuario})

def update(request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.nome = request.POST['nome']
    usuario.cpf = request.POST['cpf']
    usuario.email = request.POST['email']
    usuario.senha = request.POST['senha']
    usuario.save()
    return redirect('crud')

def delete(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('crud')


def login(request):
    form = LoginForms()

    if request.method =='POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, usuario)
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
        
    return render(request, 'login.html' , {'form': form} )
            
