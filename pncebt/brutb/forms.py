# forms.py
from django import forms
from .models import Brasil

class Propriedade(forms.Form):
    municipio = forms.ModelChoiceField(queryset=Brasil.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(Propriedade, self).__init__(*args, **kwargs)

        if user and hasattr(user, 'perfil'):
            estado_do_usuario = user.perfil.estado
            self.fields['municipio'].queryset = Brasil.objects.filter(cd_uf=estado_do_usuario)
