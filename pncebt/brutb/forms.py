from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.form.widgets import PasswordInput, TextInput
from django import forms

# Cria/registra usuário

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']

# Login User

class LoginForm(AuthenticationForm):

    username = forms.Charfield(widget=TextInput())
    password = forms.Charfield(widget=PasswordInput())
