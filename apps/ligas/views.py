from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.ligas.forms import LigaForm

# Create your views here.
def index(request):
    return render(request, 'liga/index.html' )

def liga_view(request):
    if request.method == 'POST':
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('liga:index')
    else: 
        form = LigaForm()
    
    return render(request, 'liga/liga_form.html', {'form':form})