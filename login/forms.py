# login/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulário para registro de usuário
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Usuário', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome de usuário', 'autocomplete': 'username', 'id': 'username'}), help_text='• Máximo de 20 caracteres.<br>• Letras, números e @/./+/-/_ apenas.')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha', 'autocomplete': 'new-password', 'id': 'password1', 'type': 'password'}), help_text='• Sua senha não pode ser muito parecida com o seu nome de usuário.<br>• Sua senha precisa conter pelo menos 8 caracteres.<br>• Sua senha não pode ser uma senha comumente utilizada.<br>• Sua senha não pode ser inteiramente numérica.')
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha', 'autocomplete': 'new-password', 'id': 'password2', 'type': 'password'}), help_text='• Digite novamente a senha para confirmação.')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
