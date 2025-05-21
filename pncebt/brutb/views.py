from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Propriedade
from .forms import Cadastro_Propriedade
from django.contrib import messages
import datetime
import openpyxl
import io
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.utils import timezone
from django.http import HttpResponse

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
            messages.success(
                request,
                'Propriedade cadastrada com sucesso!'
            )
            return redirect('brutb:propriedade_adiciona')
    else:
        form = Cadastro_Propriedade()

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

def exportar_propriedades(request):
    # Obtém todas as propriedades
    propriedades_lista = Propriedade.objects.select_related('veterinario').filter(estado=request.user.perfil.estado)
    # Cria um arquivo Excel
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    # Define o nome da planilha
    worksheet.title = 'Propriedades'
    # Adiciona nome dos campos como cabeçalho das colunas
    header = [field.name for field in Propriedade._meta.fields]
    print(header)
    # Adiciona cabeçalho
    worksheet.append(header)
    # Adiciona dados
    for propriedade in propriedades_lista:
        row_data = []
        for field in Propriedade._meta.fields:
            value = getattr(propriedade, field.name)
            if isinstance(field, (ForeignKey, OneToOneField)):
                value = str(value) if value else ""
            if isinstance(value, (datetime.datetime, datetime.time)):
                if timezone.is_aware(value):  # Maneira idiomática do Django
                    value = value.replace(tzinfo=None)
            row_data.append(value)
        worksheet.append(row_data)

    # Salva o arquivo Excel em memória
    saida = io.BytesIO()
    workbook.save(saida)
    saida.seek(0)
    # Retorna o arquivo em resposta HTTP
    response = HttpResponse(
        saida.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    # Configura o cabeçalho Content-Disposition para forçar o download e sugerir um nome de arquivo
    response['Content-Disposition'] = 'attachment; filename="propriedades.xlsx"'
    return response