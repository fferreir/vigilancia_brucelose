# forms.py
from django import forms
from .models import Propriedade, Municipio

class Cadastro_Propriedade(forms.ModelForm):
    #municipio = forms.ModelChoiceField(queryset=Brasil.objects.none())
    class Meta:
        model = Propriedade
        fields = '__all__'