#from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(
        max_length=2,
        choices=[('12', 'AC'),
                 ('27', 'AL' ),
                 ('13', 'AM'),
                 ('16', 'AP'),
                 ('29', 'BA'),
                 ('23', 'CE'),
                 ('53', 'DF'),
                 ('32', 'ES'),
                 ('52', 'GO'),
                 ('21', 'MA'),
                 ('31', 'MG'),
                 ('50', 'MS'),
                 ('51', 'MT'),
                 ('15', 'PA'),
                 ('25', 'PB'),
                 ('26', 'PE'),
                 ('22', 'PI'),
                 ('41', 'PR'),
                 ('33', 'RJ'),
                 ('24', 'RN'),
                 ('11', 'RO'),
                 ('14', 'RR'),
                 ('43', 'RS'),
                 ('42', 'SC'),
                 ('28', 'SE'),
                 ('35', 'SP'),
                 ('17', 'TO')],
    )
    sistema = models.CharField(
        max_length=23,
        choices=[('Brucelose', 'Brucelose'),
                 ('Tuberculose', 'Tuberculose'),
                 ('Brucelose e Tuberculose', 'Brucelose e Tuberculose')]
    )

def __str__(self):
        return f'Profile of {self.user.username}'
