from django.contrib import admin
from .models import Palestrante, Usuario, Ouvinte, Evento, Atracao

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'created', 'updated')


@admin.register(Ouvinte)
class OuvinteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'created', 'updated')


@admin.register(Palestrante)
class PalestranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'onde_trabalha')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'slug', 'data_inicial', 'data_final', 'created', 'updated')
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'palestrante', 'descricao', 'atração', 'evento', 'data', 'local', 'created', 'updated') 