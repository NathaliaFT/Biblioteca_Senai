from django.contrib import admin
from .models import Usuario
from .models import Aluguel
from .models import Livro

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Aluguel)
admin.site.register(Livro)
