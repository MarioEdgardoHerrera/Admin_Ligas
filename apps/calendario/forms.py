from django import forms

from apps.calendario.models import Calendario

class CalendarioForm(forms.ModelForm):

    class Meta:
        model = Calendario

        fields = ('nombre', 'Liga')
        labels = {
            'nombre': 'Nombre del equipo',
            'Equipo': 'Equipo',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Equipo': forms.Select(),
        }