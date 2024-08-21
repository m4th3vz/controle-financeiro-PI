# expenses/forms.py
from django import forms
from .models import Expense

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(
        label='Data',
        widget=DateInput(format='%Y-%m-%d'),
    )
    title = forms.CharField(
        label='Título',
        max_length=20,
        initial=''
    )
    duration_months = forms.IntegerField(
        label='Deseja adicionar esta despesa por quantos meses?',
        min_value=1,
        initial=1,
        max_value=48
    )
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
