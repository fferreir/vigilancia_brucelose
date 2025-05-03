#from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Perfil(models.Model):
    class Estados(models.TextChoices):
        AC = '12', 'AC'
        AL = '27', 'AL'
        AM = '13', 'AM'
        AP = '16', 'AP'
        BA = '29', 'BA'
        CE = '23', 'CE'
        DF = '53', 'DF'
        ES = '32', 'ES'
        GO = '52', 'GO'
        MA = '21', 'MA'
        MG = '31', 'MG'
        MS = '50', 'MS'
        MT = '51', 'MT'
        PA = '15', 'PA'
        PB = '25', 'PB'
        PE = '26', 'PE'
        PI = '22', 'PI'
        PR = '41', 'PR'
        RJ = '33', 'RJ'
        RN = '24', 'RN'
        RO = '11', 'RO'
        RR = '14', 'RR'
        RS = '43', 'RS'
        SC = '42', 'SC'
        SE = '28', 'SE'
        SP = '35', 'SP'
        TO = '17', 'TO'

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
        return f'Profile of {self.user.username}'
