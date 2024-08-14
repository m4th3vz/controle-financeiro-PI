# expenses/forms.py
from django import forms
from .models import Expense

# Definição de um widget personalizado para o campo de data
class DateInput(forms.DateInput):
    input_type = 'date'

# Formulário para despesa
class ExpenseForm(forms.ModelForm):
    # Sobrescreve o widget para o campo de data
    date = forms.DateField(label='Data',widget=DateInput(format='%d-%m-%Y'))
    # Campo de informações adicionais sobre o título
    title = forms.CharField(label='Título',max_length=20)
    # Campo para a duração da despesa em meses
    duration_months = forms.IntegerField(label='Deseja adicionar esta despesa por quantos meses?', min_value=1, initial=1, max_value=48)
    # Campo de informações adicionais sobre o gasto
    observation = forms.CharField(
        label='Informações adicionais sobre este gasto (Opcional):',
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
        fields = ['expense_category', 'title', 'amount', 'date', 'payment_method', 'duration_months', 'observation']
