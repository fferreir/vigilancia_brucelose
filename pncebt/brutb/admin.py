from django.contrib.gis import admin
from .models import Municipio, Propriedade
from django.contrib.admin import ShowFacets


@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ['veterinario']
    list_filter = ['veterinario']
    search_fields = ['veterinario']
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ['municipio']
    date_hierarchy = 'atualizado'
    ordering = ['veterinario', 'atualizado']
    show_facets = ShowFacets.ALWAYS

    def get_queryset(self, request):
        # Obtém o QuerySet padrão (todos os objetos)
        qs = super().get_queryset(request)

        # Se o usuário for superuser ou não tiver perfil/estado, mostra tudo
        # Adapte esta lógica conforme a sua regra de negócio para superusers/staff
        if request.user.is_superuser or not hasattr(request.user, 'perfil') or not request.user.perfil.estado:
            return qs

        # Obtém o estado do perfil do usuário logado
        estado_usuario = request.user.perfil.estado

        # Filtra o QuerySet para mostrar apenas propriedades do estado do usuário
        return qs.filter(propriedade__estado=estado_usuario)


@admin.register(Municipio)
class MunicipioAdmin(admin.GISModelAdmin):
    list_display = ('cd_mun', 'nm_mun', 'cd_uf', 'nm_uf', 'sigla_uf')
    search_fields = ('nm_mun', 'sigla_uf')