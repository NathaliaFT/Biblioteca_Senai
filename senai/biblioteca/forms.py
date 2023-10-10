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

class Login(forms.Form):
    email = forms.CharField(
        label='Email',
        required=True,
        max_length=60,
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'placeholder': "nome@email.com",
            }
        )
    )


    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "******",
            }
        )
    )