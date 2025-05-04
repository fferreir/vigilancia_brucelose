from django.contrib import admin
from .models import Propriedade

@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ['municipio', 'veterinario']
    list_filter = ['veterinario']
    search_fields = ['municipio', 'veterinario']
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ['municipio']
    date_hierarchy = 'atualizado'
    ordering = ['veterinario', 'atualizado']
    show_facets = admin.ShowFacets.ALWAYS
