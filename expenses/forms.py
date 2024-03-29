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
    # Campo de informações adicionais sobre o gasto
    observation = forms.CharField(
        label='Informações adicionais sobre este gasto:',
        max_length=60,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control mx-auto',
                'style': 'background-color: var(--cor-input); max-width: 400px;',
                'placeholder': 'Este campo é opcional',
                'rows': '6',
                'id': 'exampleFormControlTextarea1'
            }
        )
    )

    class Meta:
        model = Expense
        # Define os campos do modelo Expense que serão exibidos no formulário
        fields = ['expense_category', 'title', 'amount', 'date', 'payment_method', 'observation']

# Formulário para registro de usuário
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # Define os campos do modelo User que serão exibidos no formulário de registro
        fields = ['username', 'password1', 'password2']

# Formulário para a calculadora de empréstimo
class LoanCalculatorForm(forms.Form):
    principal = forms.DecimalField(label='Valor do Empréstimo', max_digits=10, decimal_places=2)
    taxa_juros = forms.DecimalField(label='Taxa de Juros (%)', max_digits=5, decimal_places=2)
    periodo = forms.IntegerField(label='Período (anos)')

# Formulário para a calculadora de juros simples
class SimpleInterestCalculatorForm(forms.Form):
    principal = forms.DecimalField(label='Valor Principal', max_digits=10, decimal_places=2)
    taxa_juros = forms.DecimalField(label='Taxa de Juros (%)', max_digits=5, decimal_places=2)
    periodo = forms.IntegerField(label='Período (em anos)')

# Formulário para a calculadora de juros compostos
class CompoundInterestCalculatorForm(forms.Form):
    principal = forms.DecimalField(label='Valor Principal', max_digits=10, decimal_places=2)
    taxa_juros = forms.DecimalField(label='Taxa de Juros (%)', max_digits=5, decimal_places=2)
    periodo = forms.IntegerField(label='Período (em anos)')

# Formulário para a calculadora de investimentos
class InvestmentCalculatorForm(forms.Form):
    valor_inicial = forms.DecimalField(label='Valor Inicial', max_digits=10, decimal_places=2)
    taxa_juros = forms.DecimalField(label='Taxa de Juros (%)', max_digits=5, decimal_places=2)
    periodo = forms.IntegerField(label='Período (em anos)')

# Formulário para a calculadora de prestações
class InstallmentCalculatorForm(forms.Form):
    montante = forms.DecimalField(label='Montante', max_digits=10, decimal_places=2)
    taxa_juros = forms.DecimalField(label='Taxa de Juros (%)', max_digits=5, decimal_places=2)
    periodo = forms.IntegerField(label='Período (em anos)')