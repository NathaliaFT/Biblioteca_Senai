from django.urls import path
from . import views



urlpatterns = [
    path("", views.pagina, name="index"),
    path('login', views.login_view, name="login"),
    path('registro', views.registro, name='registro'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('acao', views.acao, name="acao"),
    path('contos', views.contos, name="contos"),
    path('drama', views.drama, name="drama"),
    path('fantasia', views.fantasia, name="fantasia"),
    path('ficcao', views.ficcao, name="ficcao"),
    path('misterio', views.misterio, name="misterio"),
    path('naoficcao', views.naoficcao, name="naoficcao"),
    path('poesia', views.poesia, name="poesia"),
    path('romance', views.romance, name="romance"),
    path('terror', views.terror, name="terror"),
    # crud
    path('criar_livro/', views.criar_livro, name='criar_livro'),
    path('editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('listar/', views.listar_livros, name='listar_livros'),
    path('excluir/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),
    #crud usuarios
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir_usuario/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
]