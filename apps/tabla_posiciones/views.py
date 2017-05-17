from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.tabla_posiciones.forms import TablaForm
from .models import Tabla

# Create your views here.

def index(request):
   tabla = Tabla.objects.all()
   contexto = {'index_tabla':tabla}
   return render(request, 'tabla/index_tabla.html')
    
def tabla_view(request):
    if request.method == 'POST':
        form = TablaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_tabla')
    else: 
        form = TablaForm()
    
    return render(request, 'tabla/tabla_form.html', {'form':form})



