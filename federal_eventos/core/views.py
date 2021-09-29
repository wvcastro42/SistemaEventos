from django.views.generic import DetailView, ListView
from .models import Evento


class EventoListView(ListView):
    model = Evento

class EventoDetailView(DetailView):
    model = Evento