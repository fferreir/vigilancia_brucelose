from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
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
def lista_propriedades(request):

    propriedades = Propriedade.objects.filter(estado = request.user.perfil.estado)

    return render(request, 'brutb/propriedade/lista.html', {'propriedades': propriedades})


def detalhe_propriedade(request, id):
    try:
        propriedade = get_object_or_404( Propriedade, munic)
    except Propriedade.DoesNotExist:
        raise Http404("Propriedade não encontrada.")
    return render(
        request,
        'brutb/propriedade/detalhe.html',
        {'propriedade': propriedade}
    )