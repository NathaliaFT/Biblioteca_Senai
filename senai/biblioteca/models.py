from django.db import models


# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    id_usuario = models.IntegerField()
    email = models.TextField()
    senha = models.CharField(max_length=200)
    tipo = models.TextField()
    

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.TextField()
    autor = models.CharField(max_length=200)
    quant_pag = models.IntegerField()
    sinopse = models.TextField()
    status = models.TextField()

class Aluguel(models.Model):
    id_aluguel = models.IntegerField()
    data_retirada = models.IntegerField()
    data_entrega = models.IntegerField()

class Categoria(models.Model):
    nome = models.CharField(max_length=200)


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)