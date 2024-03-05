from django import forms
from .models import Expense

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput(format='%d-%m-%Y'))

    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date']
