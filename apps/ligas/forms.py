from django import forms

from apps.ligas.models import Liga

class LigaForm(forms.ModelForm):

    class Meta:
        model = Liga

        fields = ( 'nombre', 'telefono', 'email',)
        labels = {
            'nombre': 'Nombre de Liga',
            'telefono': 'Telefono',
            'email': 'Email',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
