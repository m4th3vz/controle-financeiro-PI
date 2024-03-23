from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Definição de um widget personalizado para o campo de data
class DateInput(forms.DateInput):
    input_type = 'date'

# Formulário para despesa
class ExpenseForm(forms.ModelForm):
    # Sobrescreve o widget para o campo de data
    date = forms.DateField(label='Data',widget=DateInput(format='%d-%m-%Y'))
    observation = forms.CharField(
        label='Informações adicionais sobre este gasto:',
        max_length=60,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control mx-auto',
                'style': 'background-color: var(--cor-input); max-width: 400px;',
                'placeholder': 'Observação',
                'rows': '6',
                'id': 'exampleFormControlTextarea1'
            }
        )
    )

    class Meta:
        model = Expense
        # Define os campos do modelo Expense que serão exibidos no formulário
        fields = ['title', 'amount', 'date', 'payment_method', 'observation']

# Formulário para registro de usuário
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # Define os campos do modelo User que serão exibidos no formulário de registro
        fields = ['username', 'password1', 'password2']
