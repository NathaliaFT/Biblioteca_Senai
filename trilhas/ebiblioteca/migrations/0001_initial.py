# Generated by Django 4.2.6 on 2023-10-22 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('capa', models.ImageField(upload_to='livros/')),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('data_de_nascimento', models.DateField()),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_aluguel', models.DateTimeField(auto_now_add=True)),
                ('data_de_devolucao', models.DateTimeField()),
                ('devolvido', models.BooleanField(default=False)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebiblioteca.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebiblioteca.usuario')),
            ],
        ),
    ]
