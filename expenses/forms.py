from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Este arquivo é usado para criar e definir formulários HTML, que são usados para coletar e validar dados de entrada do usuário.
# Os formulários definidos neste arquivo podem ser usados para criar e atualizar objetos do banco de dados definidos em models.py.
# Os formulários podem incluir campos extras, validações personalizadas e lógica de processamento de dados para garantir que os dados inseridos pelo usuário sejam válidos antes de serem salvos no banco de dados.

# Definição de um widget personalizado para o campo de data
class DateInput(forms.DateInput):
    input_type = 'date'

# Formulário para despesa
class ExpenseForm(forms.ModelForm):
    # Sobrescreve o widget para o campo de data
    date = forms.DateField(label='Data',widget=DateInput(format='%d-%m-%Y'))
    # Campo de informações adicionais sobre o título
    title = forms.CharField(label='Título',max_length=20)
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
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome de usuário', 'autocomplete': 'username', 'id': 'username'}), help_text='• Máximo de 150 caracteres.<br>• Letras, números e @/./+/-/_ apenas.')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha', 'autocomplete': 'new-password', 'id': 'password1', 'type': 'password'}), help_text='• Sua senha não pode ser muito parecida com o seu nome de usuário.<br>• Sua senha precisa conter pelo menos 8 caracteres.<br>• Sua senha não pode ser uma senha comumente utilizada.<br>• Sua senha não pode ser inteiramente numérica.')
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha', 'autocomplete': 'new-password', 'id': 'password2', 'type': 'password'}), help_text='• Digite novamente a senha para confirmação.')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Formulário para a calculadora de empréstimo
class LoanCalculatorForm(forms.Form):
    principal = forms.DecimalField(
        label='Valor do Empréstimo',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    taxa_juros = forms.DecimalField(
        label='Taxa de Juros (%)',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    periodo = forms.IntegerField(
        label='Período (anos)',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )

# Formulário para a calculadora de juros simples
class SimpleInterestCalculatorForm(forms.Form):
    principal = forms.DecimalField(
        label='Valor Principal',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    taxa_juros = forms.DecimalField(
        label='Taxa de Juros (%)',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    periodo = forms.IntegerField(
        label='Período (anos)',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )

# Formulário para a calculadora de juros compostos
class CompoundInterestCalculatorForm(forms.Form):
    principal = forms.DecimalField(
        label='Valor Principal',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    taxa_juros = forms.DecimalField(
        label='Taxa de Juros (%)',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    periodo = forms.IntegerField(
        label='Período (anos)',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )

# Formulário para a calculadora de investimentos
class InvestmentCalculatorForm(forms.Form):
    principal = forms.DecimalField(
        label='Valor Inicial',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    taxa_juros = forms.DecimalField(
        label='Taxa de Juros (%)',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    periodo = forms.IntegerField(
        label='Período (anos)',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )

# Formulário para a calculadora de prestações
class InstallmentCalculatorForm(forms.Form):
    principal = forms.DecimalField(
        label='Montante',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    taxa_juros = forms.DecimalField(
        label='Taxa de Juros (%)',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )
    periodo = forms.IntegerField(
        label='Período (anos)',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center', 'style': 'background-color: var(--cor-input)'})
    )