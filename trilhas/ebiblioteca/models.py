from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Modelo para os livros na biblioteca
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50, default='Desconhecido')
    capa = models.ImageField(upload_to='livros/')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

# Modelo para os usuários da biblioteca
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_de_nascimento = models.DateField()
    data_de_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Modelo para os aluguéis de livros
class Aluguel(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_de_aluguel = models.DateTimeField(auto_now_add=True)
    data_de_devolucao = models.DateTimeField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.nome} alugou {self.livro.titulo}"
