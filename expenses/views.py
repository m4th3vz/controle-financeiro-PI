from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

def expense_list(request):
    expenses = Expense.objects.all()
    total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0  # Calcule a soma total das despesas
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_expenses': total_expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
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

