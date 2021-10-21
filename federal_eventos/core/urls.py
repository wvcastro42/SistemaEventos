from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [

    # eventos
    path('', views.EventoListView.as_view(), name='list'),
    path('<slug:slug>/', views.EventoDetailView.as_view(), name='detail'),
    path('create/', views.EventoCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.EventoUpdateView.as_view(), name='update'),

    # atrações
    path('detail-atracao/<int:pk>', views.AtracaoDetailView.as_view(), name='detail-atracao'),
]