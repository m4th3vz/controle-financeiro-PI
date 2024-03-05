from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput(format='%d-%m-%Y'))

    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
