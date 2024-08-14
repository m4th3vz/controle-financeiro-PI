# calculator/forms.py
from django import forms

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