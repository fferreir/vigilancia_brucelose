from django.db import models
from django.contrib.auth.models import User

class Conta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(
        max_length=2,
        choices=[('AC', 'AC'),
                 ('AL', 'AL'),
                 ('AM', 'AM'),
                 ('AP', 'AP'),
                 ('BA', 'BA'),
                 ('CE', 'CE'),
                 ('DF', 'DF'),
                 ('ES', 'ES'),
                 ('GO', 'GO'),
                 ('MA', 'MA'),
                 ('MG', 'MG'),
                 ('MS', 'MS'),
                 ('MT', 'MT'),
                 ('PA', 'PA'),
                 ('PB', 'PB'),
                 ('PE', 'PE'),
                 ('PI', 'PI'),
                 ('PR', 'PR'),
                 ('RJ', 'RJ'),
                 ('RN', 'RN'),
                 ('RO', 'RO'),
                 ('RR', 'RR'),
                 ('RS', 'RS'),
                 ('SC', 'SC'),
                 ('SE', 'SE'),
                 ('SP', 'SP'),
                 ('TO', 'TO')],
    )
    sistema = models.CharField(
        max_length=23,
        choices=[('Brucelose', 'Brucelose'),
                 ('Tuberculose', 'Tuberculose'),
                 ('Brucelose e Tuberculose', 'Brucelose e Tuberculose')]
    )

def __str__(self):
        return self.user.username
