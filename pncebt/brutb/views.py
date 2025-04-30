from django.shortcuts import render
from django.http import HttpResponse
from .forms import Propriedade

@login_required
def home(request):

    return render(request, 'brutb/index.html')

@login_required
def propriedade_view(request):
    if request.method == 'POST':
        form = Propriedade(request.POST, user=request.user)
        if form.is_valid():
            # Processa os dados aqui
            pass
    else:
        form = Propriedade(user=request.user)

    return render(request, 'brutb/propriedade.html', {'form': form})