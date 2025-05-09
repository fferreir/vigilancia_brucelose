from django.contrib.gis.db import models
from django.conf import settings
from conta.models import Perfil

class Brasil(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # Brazil's shapefile.
    cd_mun = models.CharField(max_length=7, primary_key=True)
    nm_mun = models.CharField(max_length=100)
    cd_uf = models.CharField(max_length=2)
    nm_uf = models.CharField(max_length=50)
    sigla_uf = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=4674)

    class Meta:
        ordering = ['cd_uf', 'nm_mun']
        indexes = [
            models.Index(fields=['cd_uf', 'nm_mun']),
        ]

    def __str__(self):
        return self.nm_mun

class Propriedade(models.Model):
    # Fields corresponding to the attributes in the questionary
    estado = models.CharField(max_length=2)
    municipio = models.ForeignKey(Brasil, on_delete=models.PROTECT)
    veterinario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='registros_propriedades'
    )
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['municipio']
        indexes = [
            models.Index(fields=['municipio']),
        ]

    def __str__(self):
        return self.municipio

