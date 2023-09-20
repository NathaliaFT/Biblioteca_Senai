from django.contrib import admin
from .models import Usuario
from .models import Livro
from .models import Aluguel
# Register your models here.

admin.site.register(Usuario)

admin.site.register(Livro)

admin.site.register(Aluguel)
