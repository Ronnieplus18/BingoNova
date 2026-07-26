from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del jugador'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu nombre'
            })
        }