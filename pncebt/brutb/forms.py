# forms.py
from django import forms
from .models import Brasil

class Propriedade(forms.Form):
    #municipio = forms.ModelChoiceField(queryset=Brasil.objects.none())
    estado = forms.CharField(max_length=2)
    veterinario = forms.CharField(max_length=100)

