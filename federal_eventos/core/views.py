from django.views.generic import DetailView, ListView
from .models import Evento, Atracao
from django.http import HttpResponse
import datetime
from django.urls import reverse_lazy


class EventoListView(ListView):
    model = Evento


class EventoDetailView(DetailView):
    model = Evento


class AtracaoDetailView(DetailView):
    model = Atracao
    success_url = reverse_lazy('core:detail-atracao')

def current_datetime(request):
    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    html = '<html><body>Here is the index page. It is now %s.</body></html>' %now
    return HttpResponse(html)


