from django import forms

class Newsletter(forms.Form):
    email_news = forms.CharField(
        label='Newsletter',
        required=False,
        max_length= 100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email para receber novidades',
            }
        )
    )

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )


class LivroForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=100)
    autor = forms.CharField(label='Autor', max_length=100)
    publicação = forms.DateField(label='Data de Publicação')
    paginas = forms.IntegerField(label='Número de Páginas')
    capa = forms.ImageField(label='Capa do Livro')