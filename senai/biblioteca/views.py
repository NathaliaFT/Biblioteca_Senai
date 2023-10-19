from django.shortcuts import render, redirect
from .models import Usuario, Tarefa
from .forms import Newsletter
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import LoginForms
from .forms import LivroForm
from .models import Livro, Categoria


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
        return redirect('loginn')

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

def adicionar_livro(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST, request.FILES)
        if livro_form.is_valid():
            novo_livro = Livro(
                titulo= livro_form.cleaned_data['titulo'],
                autor= livro_form.cleaned_data['autor'],
                publicação= livro_form.cleaned_data['publicação'],
                paginas= livro_form.cleaned_data['paginas'],
                capa = livro_form.cleaned_data['capa']
            )
            novo_livro.save() 

            return redirect('lista_livros')
    else:
        livro_form = LivroForm()

    return render(request, 'adicionar_livro.html', {'livro_form': livro_form})

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

def registro(request):
    return render(request, "registro.html")

def login(request):
    form = LoginForms()

    if request.method =='POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request,
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





def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def livro_detalhes (request):
    livros = livros.objects.all()
    return render(request, 'livro_detalhes.html', {'livros': livros})

def nov(request):
    if request.method =="POST":
        bd = Categoria(nome=request.POST['email_news'])
        bd.save()
        messages.success(request, f'email cadastrado com sucessos!')
        return redirect('index')