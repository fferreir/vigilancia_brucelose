from django.contrib.gis.db import models

class Brasil(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # Brazil's shapefile.
    cd_mun = models.CharField(max_length=7)
    nm_mun = models.CharField(max_length=100)
    cd_uf = models.CharField(max_length=2)
    nm_uf = models.CharField(max_length=50)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPolygonField(srid=4674)

    # Returns the string representation of the model.
    def __str__(self):
        return self.nm_mun

