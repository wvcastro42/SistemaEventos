from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
import uuid

class Ouvinte(models.Model):
    # nome = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True)
    # password = models.CharField(max_length=16, blank=True)
    email = models.CharField(max_length=249, default=None, blank=True, null=True)
    confirmado = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.usuario.username)

    class Meta:
        verbose_name = 'Ouvinte'
        verbose_name_plural = 'Ouvintes'
        ordering = ("-created",)


class Palestrante(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    profissao = models.CharField(max_length=50, blank=False)
    onde_trabalha = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

    
class Evento(models.Model):
    nome = models.CharField(max_length=150, blank=False, null=True)
    descricao = models.TextField(default='Insira a descrição')
    data_inicial = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ("-created",)
    

    def get_absolute_url(self):
        return reverse("core:detail", kwargs={'slug': self.slug})


class Atracao(models.Model):
    
    # imagem da atração?
    customer_types = (
        (1,'Palestra'),
        (2,'Workshop'),
        (3,'Encontro'),
        (4,'Seminário'),
        (5,'Mesa-redonda'),
        (6,'Simpósio'),
        (7,'Painel'),
        (8,'Fórum'),
        (9,'Conferência'),
        (10,'Jornada'),
        (11,'Cursos'),
        (12,'Colóquio'),
        (13,'Semana'),
    )
    atração = models.IntegerField(choices=customer_types, default=1)
    nome = models.CharField(max_length=150, blank=False, null=True)
    descricao = models.TextField(blank=False, null=True)
    palestrante = models.ForeignKey(Palestrante, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data = models.DateField(blank=False, null=True)
    local = models.CharField(max_length=50, default='IFSP JCR')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
        ordering = ("-created",)


class Inscricao(models.Model):
    atracao = models.ForeignKey(Atracao, on_delete=models.CASCADE, related_name="incricoes")
    ouvinte = models.ForeignKey(Ouvinte, on_delete=models.CASCADE, related_name="ouvintes")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 


    def __str__(self):
        return f'{self.ouvinte.usuario.username} - {self.atracao.nome}'



