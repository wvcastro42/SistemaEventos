from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from cpf_field.models import CPFField
from django.contrib.auth.forms import UserCreationForm
from core.models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'


class UserForm(UserCreationForm):
    cpf = CPFField('cpf')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'cpf']
