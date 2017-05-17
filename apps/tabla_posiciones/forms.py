from django import forms

from apps.tabla_posiciones.models import Tabla

class TablaForm(forms.ModelForm):

    class Meta:
        model = Tabla

        fields = (
        'posicion',
        'Equipos',
        'juegos_jugados',
        'juegos_ganados',
        'juegos_empatados',
        'juegos_perdidos',
        'goles_anotados',
        'goles_permitidos',
        'diferencia_goles',
        'puntos'
        )
        labels = {
            'posicion':'Posición',
            'Equipos':'Equipo',
            'juegos_jugados':'JJ',
            'juegos_ganados':'JG',
            'juegos_empatados':'JE',
            'juegos_perdidos':'JP',
            'goles_anotados':'GA',
            'goles_permitidos':'GP',
            'diferencia_goles':'DG',
            'puntos':'Pts',

        }
        widgets = {
            'posicion': forms.TextInput(attrs={'class': 'form-control'}),
            'Equipos':forms.TextInput(attrs={'class':'form-control'}),
            'juegos_jugados':forms.TextInput(attrs={'class':'form-control'}),
            'juegos_ganados':forms.TextInput(attrs={'class':'form-control'}),
            'juegos_empatados':forms.TextInput(attrs={'class':'form-control'}),
            'juegos_perdidos':forms.TextInput(attrs={'class':'form-control'}),
            'goles_anotados':forms.TextInput(attrs={'class':'form_control'}),
            'goles_permitidos':forms.TextInput(attrs={'class':'form-control'}),
            'diferencia_goles':forms.TextInput(attrs={'class':'form-control'}),
            }