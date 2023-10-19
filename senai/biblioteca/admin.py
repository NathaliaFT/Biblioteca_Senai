from django.contrib import admin
from .models import Usuario
from .models import Livro
from .models import Aluguel
# Register your models here.

admin.site.register(Usuario)

admin.site.register(Livro)

admin.site.register(Aluguel)


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicação')
    list_filter = ('autor', 'publicação')
    search_files = ('titulo', 'autor')
    fieldsets = [
        ('Inforações Básicas', {'fields': ['titulo', 'autor', 'publicação']}),
        ('Detalhes Adicionais', {'fields': ['paginas', 'capas']}),
    ]
