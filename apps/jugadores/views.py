from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.jugadores.forms import JugadoresForm

from .models import Jugadores
# Create your views here.

def index(request):
    jugadores = Jugadores.objects.all()
    return render(request, 'jugadore/index_jugadore.html', {'jugadores':jugadores})

def jugadores_view(request):
    '''Muesta detalles de los Jugadores'''
    if request.method == 'POST':
        form = JugadoresForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_jugadore')
    else:
        form = JugadoresForm()

    return render(request, 'jugadore/jugadore_form.html', {'form':form})