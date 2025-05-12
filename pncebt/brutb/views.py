from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Propriedade

@login_required
def home(request):

    return render(request, 'brutb/index.html')

@login_required
def propriedade(request):
    if request.method == 'POST':
        form = Propriedade(request.POST)
        if form.is_valid():
            # Processa os dados aqui
            pass
    else:
        form = Propriedade()

    return render(request, 'brutb/propriedade.html', {'post': post,
                                                      'form': form})

def lista_propriedades(request):
    # Obtém todas as propriedades
    propriedades = Propriedade.objects.all()
    return render(request, 'brutb/propriedade/lista.html', {'propriedades': propriedades})

def propriedade_detalhe(request, pk):
    # Obtém uma propriedade específica
    propriedade = get_object_or_404(Propriedade, pk=pk)
    return render(request, 'brutb/propriedade/detalhe.html', {'propriedade': propriedade})

