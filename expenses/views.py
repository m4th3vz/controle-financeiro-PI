from .models import Expense
from .forms import ExpenseForm, UserRegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)  # Filtrando as despesas pelo usuário atual
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_expenses': total_expenses})


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Associando a despesa ao usuário atual
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})

def delete_all_expenses(request):
    if request.method == 'POST':
        Expense.objects.all().delete()
        return redirect('expense_list')
    return redirect('confirm_delete_expenses')

def confirm_delete_expenses(request):
    return render(request, 'expenses/confirm_delete.html')

def calculator(request):
    return render(request, 'calculator.html')

def calculator(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        if expression:
            try:
                result = eval(expression)
            except Exception as e:
                result = f"Error: {str(e)}"
            return render(request, 'calculator.html', {'result': result})
    return render(request, 'calculator.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})