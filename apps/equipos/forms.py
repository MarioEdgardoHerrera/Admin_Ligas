from django import forms

from apps.equipos.models import Equipos

class EquiposForm(forms.ModelForm):

    class Meta:
        model = Equipos

        fields = ('nombre', 'Liga')
        labels = {
            'nombre': 'Nombre del equipo',
            'Liga': 'Liga',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Liga': forms.Select(),
        }
