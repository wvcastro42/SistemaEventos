from django.views.generic import DetailView, ListView, CreateView, DeleteView, TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
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


# def current_datetime(request):
#     now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
#     html = '<html><body>Here is the index page. It is now %s.</body></html>' %now
#     return HttpResponse(html)
