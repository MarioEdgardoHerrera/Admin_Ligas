from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.ligas.forms import LigaForm
from .models import Liga

# Create your views here.
def index(request):
    # Aqui vamos a cargar las ligas que están en la base de datos
    ligas = Liga.objects.all # Creo que se entiende verdad?
    return render(request, 'liga/index.html', {'ligas': ligas}) 
    # Esto es sencillo: Rendereamos el template y de paso le mandamos el objeto con todas las ligas



def liga_view(request):
    if request.method == 'POST':
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else: 
        form = LigaForm()
    
    return render(request, 'liga/liga_form.html', {'form':form})