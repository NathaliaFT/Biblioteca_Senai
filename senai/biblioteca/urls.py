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
    path("index.html", views.index, name="index")

]