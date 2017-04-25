from django import forms

from apps.jugadores.models import Jugadores

class JugadoresForm(forms.ModelForm):

    class Meta:
        model = Jugadores

        fields = ('nombre', 'apellido', 'edad',)
        labels = {
            'nombre': 'Nombre del Jugador',
            'apellido': 'Apellido',
            'edad': 'Edad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
        }