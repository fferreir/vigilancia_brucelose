from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Propriedade
from .forms import Cadastro_Propriedade

@login_required
def home(request):

    return render(request, 'brutb/index.html')

@login_required
def propriedade(request):

    if request.method == 'POST':
        form = Cadastro_Propriedade(request.POST)
        if form.is_valid():
            # Processa os dados aqui
            form.save()
            return redirect('propriedade_adiciona')
    else:
        form = Propriedade()

    context = {
        'form': form
    }

    return render(request, 'brutb/propriedade/adiciona.html', context=context)

@login_required
def lista_propriedades(request):
    # Obtém todas as propriedades
    propriedades_lista = Propriedade.objects.select_related('veterinario').filter(estado=request.user.perfil.estado)
    # Paginador com 3 posts por página
    paginator = Paginator(propriedades_lista, 3)
    page_number = request.GET.get('page', 1)
    propriedades = paginator.page(page_number)
    return render(request, 'brutb/propriedade/lista.html', {'propriedades': propriedades})

@login_required
def propriedade_detalhe(request, cod_rebanho_estudo):
    # Obtém uma propriedade específica
    propriedade = get_object_or_404(Propriedade, cod_rebanho_estudo=cod_rebanho_estudo)
    return render(request, 'brutb/propriedade/detalhe.html', {'propriedade': propriedade})

