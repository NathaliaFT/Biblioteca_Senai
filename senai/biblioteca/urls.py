from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("infantil.html", views.infantil, name="infantil"),
    path("romance.html", views.romance, name="Romance"),
    path("Fantasia.html", views.Fantasia, name="Fantasia"),
    path("Fic.html", views.Fic, name="Fic"),
    path("carrinho.html", views.carrinho, name="carrinho"),
    path("index.html", views.index, name="index"),
    path("login", views.login, name="login"),
    path("forms.html/", views.forms, name="forms"),
    path("novidade", views.nov, name="novidade"),
    path('deletar/<int:id>', views.delete, name="delete"),
    path('listar/', views.lista_tarefas, name='lista_tarefas'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('atualizar/<int:pk>/', views.atualizar_tarefa, name='atualizar_tarefa'),
    path('excluir/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
    

]