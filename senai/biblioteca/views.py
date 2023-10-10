from django.shortcuts import render, redirect
from .models import *
from biblioteca.forms import *
from django.contrib import messages
from .models import Tarefa

from django.shortcuts import render, get_object_or_404, redirect

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

def forms(request):
    return render (request, 'forms.html')

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

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})



def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'criar_tarefa.html', {'form': form})


def atualizar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'atualizar_tarefa.html', {'form': form})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('lista_tarefas')