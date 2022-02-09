from django.views.generic import DetailView, ListView, CreateView, DeleteView, TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render

from core.form import UserForm
from .models import Evento, Atracao
from django.http import HttpResponse
from django.urls import reverse_lazy
import datetime


class EventoListView(ListView):
    model = Evento


class EventoDetailView(DetailView):
    model = Evento


class EventoCreateView(CreateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('core:detail')


class EventoUpdateView(UpdateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('core:list')


class AtracaoDetailView(DetailView):
    model = Atracao
    success_url = reverse_lazy('core:detail-atracao')


class HomePageView(TemplateView):
    template_view = "home.html"


class UserCreate(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de Novo Usuário"
        context['botao'] = "Cadastrar"

        return context