from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Propriedade
from .models import Propriedade

@login_required
def home(request):

    return render(request, 'brutb/index.html')

@login_required
def propriedade(request):
    if request.method == 'POST':
        form = Propriedade(request.POST, user=request.user)
        if form.is_valid():
            # Processa os dados aqui
            pass
    else:
        form = Propriedade(user=request.user)

    return render(request, 'brutb/propriedade.html', {'form': form})

@login_required
def propriedades_registradas_por_estado(request):

    registros_do_estado = Propriedade.objects.para_estado_usuario(request.user)

    context = {
        'registros_do_estado': registros_do_estado,
    }
    return render(request, 'brutb/propriedades_registradas.html', context)