from django.shortcuts import render
from django.http import HttpResponse
#crud
from django.shortcuts import render, redirect
from .forms import LivroForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from django.shortcuts import render, get_object_or_404, redirect
#crud usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect



@login_required


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirecionar após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecione o usuário para a página de sucesso após o login.
            return redirect('dashboard.html')  # Substitua 'pagina_de_sucesso' pela sua página de sucesso.
        else:
            # Exiba uma mensagem de erro se as credenciais estiverem incorretas.
            error_message = "Credenciais inválidas. Tente novamente."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    


def pagina(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def acao(request):
    return render(request, 'acao.html')

def contos(request):
    return render(request, 'contos.html')

def drama(request):
    return render(request, 'drama.html')

def fantasia(request):
    return render(request, 'fantasia.html')

def ficcao(request):
    return render(request, 'ficcao.html')

def misterio(request):
    return render(request, 'misterio.html')

def naoficcao(request):
    return render(request, 'nao-ficcao.html')

def poesia(request):
    return render(request, 'poesia.html')

def romance(request):
    return render(request, 'romance.html')

def terror(request):
    return render(request, 'terror.html')

#crud


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html', {'livros': livros})

def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'detalhes_livro.html', {'livro': livro})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'criar_livro.html', {'form': form})

def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')  # Redireciona para a lista de livros após a edição
    else:
        form = LivroForm(instance=livro)

    return render(request, 'editar_livro.html', {'form': form, 'livro': livro})

def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')  # Redireciona para a lista de livros após a exclusão
    
    return render(request, 'excluir_livro.html', {'livro': livro})

#crud usuario

def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        # Processar o formulário de criação de usuário
        # Lembre-se de validar os dados do formulário
        User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        return redirect('listar_usuarios')
    return render(request, 'criar_usuario.html')

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    if request.method == 'POST':
        # Processar o formulário de edição de usuário
        # Lembre-se de validar os dados do formulário
        usuario.username = request.POST['username']
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'editar_usuario.html', {'usuario': usuario})

def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    usuario.delete()
    return redirect('listar_usuarios')

