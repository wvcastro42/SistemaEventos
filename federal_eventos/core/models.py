from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=50, default='Admin')
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Ouvinte(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=10, blank=True)
    password = models.CharField(max_length=16, blank=True)
    confirmado = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ouvinte'
        verbose_name_plural = 'Ouvintes'
