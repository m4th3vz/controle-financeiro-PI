# expenses/views.py
from .models import Expense, UserProfile
from .forms import ExpenseForm
from decimal import Decimal, InvalidOperation
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

# Lista de despesas
@login_required
def expense_list(request, year=None, month=None):
    if request.method == 'POST':
        salary = request.POST.get('salary')

        # Verifica se o campo de renda mensal está vazio ou não é um número
        if not salary:
            salary = Decimal('0.00')  # Define a renda mensal como 0.00 se estiver vazio
        else:
            try:
                salary = Decimal(salary)  # Tenta converter o valor da renda mensal para Decimal
            except (ValueError, InvalidOperation):
                # Se ocorrer um erro de conversão, define o valor como zero
                salary = Decimal('0.00')

        # Salva a renda mensal associada ao usuário logado
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.salary = salary
        user_profile.save()

    if year is None or month is None:
        # Se nenhum ano ou mês for fornecido, use o ano e mês atuais
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month

    # Converte ano e mês para o tipo inteiro
    year = int(year)
    month = int(month)

    # Lógica para cálculo do mês anterior
    prev_month = month - 1
    prev_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year -= 1

    # Lógica para cálculo do próximo mês
    next_month = month + 1
    next_year = year
    if next_month == 13:
        next_month = 1
        next_year += 1

    expenses = Expense.objects.filter(user=request.user, date__year=year, date__month=month)

    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = round(total_expenses, 2)

    salary = UserProfile.objects.get(user=request.user).salary if UserProfile.objects.filter(user=request.user).exists() else None
    
    # Calcula a diferença entre a renda mensal e o total das despesas
    difference = salary - total_expenses if salary is not None else None

    # Calcular a soma das despesas para cada categoria
    expenses_by_category = Expense.objects.filter(user=request.user, date__year=year, date__month=month).values('expense_category').annotate(total_amount=Sum('amount'))
    
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_expenses': total_expenses, 'salary': salary, 'difference': difference, 'expenses_by_category': expenses_by_category, 'year': year, 'month': month, 'prev_year': prev_year, 'prev_month': prev_month, 'next_year': next_year, 'next_month': next_month})

# Adicionar despesa
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()

            # Se a duração da despesa for maior que 1, crie despesas para cada mês adicional
            for i in range(expense.duration_months - 1):
                # Clona a despesa original e ajusta a data
                new_expense = Expense.objects.create(
                    expense_category=expense.expense_category,
                    title=expense.title,
                    amount=expense.amount,
                    date=expense.date + timedelta(days=30 * (i + 1)),  # Adiciona 30 dias para cada mês adicional
                    payment_method=expense.payment_method,
                    observation=expense.observation,
                    user=request.user,
                    duration_months=1  # Define a duração como 1 para cada despesa adicional
                )

            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

# Excluir despesa
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})

# Excluir todas as despesas
@login_required
def delete_all_expenses(request):
    # Verificar se o método da requisição é POST
    if request.method == 'POST':
        # Excluir todas as despesas do usuário logado
        Expense.objects.filter(user=request.user).delete()
        return redirect('expense_list')
    return redirect('confirm_delete_expenses')

# Confirmar exclusão de todas as despesas
@login_required
def confirm_delete_expenses(request):
    return render(request, 'expenses/confirm_delete.html')
