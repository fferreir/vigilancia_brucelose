from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Perfil(models.Model):
    class Estados(models.TextChoices):
        AC = 'AC', 'AC'
        AL = 'AL', 'AL'
        AM = 'AM', 'AM'
        AP = 'AP', 'AP'
        BA = 'BA', 'BA'
        CE = 'CE', 'CE'
        DF = 'DF', 'DF'
        ES = 'ES', 'ES'
        GO = 'GO', 'GO'
        MA = 'MA', 'MA'
        MG = 'MG', 'MG'
        MS = 'MS', 'MS'
        MT = 'MT', 'MT'
        PA = 'PA', 'PA'
        PB = 'PB', 'PB'
        PE = 'PE', 'PE'
        PI = 'PI', 'PI'
        PR = 'PR', 'PR'
        RJ = 'RJ', 'RJ'
        RN = 'RN', 'RN'
        RO = 'RO', 'RO'
        RR = 'RR', 'RR'
        RS = 'RS', 'RS'
        SC = 'SC', 'SC'
        SE = 'SE', 'SE'
        SP = 'SP', 'SP'
        TO = 'TO', 'TO'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(
        max_length=2,
        choices=Estados
    )
    sistema = models.CharField(
        max_length=23,
        choices=[('Brucelose', 'Brucelose'),
                 ('Tuberculose', 'Tuberculose'),
                 ('Brucelose e Tuberculose', 'Brucelose e Tuberculose')]
    )

    def __str__(self):
        return f'{self.user.username}'
