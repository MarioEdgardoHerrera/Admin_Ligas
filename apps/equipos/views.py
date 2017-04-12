from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index_equipos(request):
    return HttpResponse("Pagina principal de equipo")