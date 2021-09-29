from django.db import models
from django.urls import reverse

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=50, default='Admin')
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ("-created",)


class Ouvinte(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, blank=True)
    password = models.CharField(max_length=16, blank=True)
    email = models.CharField(max_length=249, default=None)
    confirmado = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

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
    # atracoes = models.on
    # CRIAR HASH
    #criar imagem do evento?

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ("-created",)
    
    def get_absolute_url(self):
        return reverse("core:detail", kwargs={'slug': self.slug})


class Atracao(models.Model):
    # CRIAR HASH
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