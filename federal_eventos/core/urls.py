from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.EventoListView.as_view(), name='list'),
    path('<slug:slug>/', views.EventoDetailView.as_view(), name='detail'),
]