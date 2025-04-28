from django.shortcuts import render
from django.http import HttpResponse
from .forms import Propriedade
def home(request):

    return render(request, 'brutb/index.html')


def propriedade_view(request):
    if request.method == 'POST':
        form = Propriedade(request.POST, user=request.user)
        if form.is_valid():
            # Processa os dados aqui
            pass
    else:
        form = Prorpriedade(user=request.user)

    return render(request, 'propriedade.html', {'form': form})