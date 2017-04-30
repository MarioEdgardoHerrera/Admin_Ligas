from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.equipos.forms import EquiposForm
from .models import Equipos

# Create your views here.

def index(request):
    equipos = Equipos.objects.all() 
    return render(request, 'equipo/index_equipo.html', {'equipos': equipos}) 
    
def equipo_view(request):
    if request.method == 'POST':
        form = EquiposForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_equipos')
    else: 
        form = EquiposForm()
    
    return render(request, 'equipo/equipo_form.html', {'form':form})



