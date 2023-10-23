from django import forms
from .models import Livro
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'



class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # Adicione outros campos personalizados aqui

    class Meta:
        model = Usuario  # Use seu modelo de usuário personalizado
        fields = '__all__'



