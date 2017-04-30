from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.tabla_posiciones.forms import TablaForm
from .models import Tabla

# Create your views here.

def index(request):
    
    return render(request, 'tabla_posiciones/index_tabla.html')
    
def tabla_view(request):
    if request.method == 'POST':
        form = TablaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_tabla')
    else: 
        form = TablaForm()
    
    return render(request, 'tabla_posiciones/tabla_form.html', {'form':form})

def tabla_list(request):
    tabla = Tabla.objects.all()
    contexto = {'tabla_posiciones':tabla}
    return render(request, 'tabla/tabla.html', contexto)

