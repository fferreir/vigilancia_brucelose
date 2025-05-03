from django.contrib.gis.db import models
from django.conf import settings

class Brasil(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # Brazil's shapefile.
    cd_mun = models.CharField(max_length=7)
    nm_mun = models.CharField(max_length=100)
    cd_uf = models.CharField(max_length=2)
    nm_uf = models.CharField(max_length=50)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPolygonField(srid=4674)

    def __str__(self):
        return self.nm_mun

class Propriedades(models.Model):
    # Fields corresponding to the attributes in the questionary
    municipio = models.ForeignKey(Brasil, on_delete=models.PROTECT)
    veterinario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='registros_propriedades'
    )
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    # Returns the string representation of the model.
    def __str__(self):
        return self.municipio

