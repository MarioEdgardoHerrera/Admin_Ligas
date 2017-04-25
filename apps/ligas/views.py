
from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ligas.forms import LigaForm

from .models import Liga


# Create your views here.
def index(request):
    '''Muestra la pagina inicial'''
    # Aqui vamos a cargar las ligas que están en la base de datos
    ligas = Liga.objects.all # Creo que se entiende verdad?
    return render(request, 'liga/index.html', {'ligas': ligas})
    # Esto es sencillo: Rendereamos el template y de paso le mandamos el objeto con todas las ligas



def liga_view(request):
    '''Muesta detalles de las ligas'''
    if request.method == 'POST':
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ver_index')
    else:
        form = LigaForm()

    return render(request, 'liga/liga_form.html', {'form':form})
