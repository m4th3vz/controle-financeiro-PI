from .models import Expense, UserProfile
from .forms import ExpenseForm, UserRegistrationForm, LoanCalculatorForm, SimpleInterestCalculatorForm, CompoundInterestCalculatorForm, InvestmentCalculatorForm, InstallmentCalculatorForm
from decimal import Decimal, InvalidOperation
import datetime
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta

# As views podem realizar uma variedade de tarefas, como recuperar dados do banco de dados, validar dados de entrada do usuário, realizar cálculos e renderizar templates.

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
            # Salva a despesa associada ao usuário logado
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

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

# Página da calculadora
@login_required
def calculator(request):
    return render(request, 'calculator.html')

# Personalização da página de login
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('welcome')
    
# Página de registro de usuário
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Adiciona mensagens de erro ao contexto
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Página de boas-vindas
@login_required
def welcome(request):
    return render(request, 'welcome.html')

# Página de sobre
@login_required
def about(request):
    return render(request, 'about.html')

# Página da lista de calculadoras
@login_required
def calc_list(request):
    return render(request, 'calc_list.html')

#--------------------------------------#
# Função para Calcular Empréstimo
def calculadora_de_emprestimo(principal, taxa_juros, periodo):
    taxa_juros_mensal = taxa_juros / 100 / 12
    num_pagamentos = periodo * 12

    # Calcular o pagamento mensal de empréstimos
    pagamento_mensal = (principal * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_pagamentos)

    return round(pagamento_mensal, 2)

# Esta view é uma aplicação Django e coordena a interação do usuário com a interface web
@login_required
def calc_loan(request):
    if request.method == 'POST':
        form = LoanCalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            pagamento_mensal = calculadora_de_emprestimo(principal, taxa_juros, periodo)
            return render(request, 'calc_loan.html', {'form': form, 'pagamento_mensal': pagamento_mensal})
    else:
        form = LoanCalculatorForm()
    return render(request, 'calc_loan.html', {'form': form})

#--------------------------------------#
# Função para Calcular Juros Simples
def juros_simples(principal, taxa_juros, periodo):
    juros = principal * (taxa_juros / 100) * periodo
    montante = principal + juros
    return round(montante, 2)

# View para a calculadora de juros simples
@login_required
def calc_simple_interest(request):
    if request.method == 'POST':
        form = SimpleInterestCalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = juros_simples(principal, taxa_juros, periodo)
            return render(request, 'calc_simple_interest.html', {'form': form, 'montante': montante})
    else:
        form = SimpleInterestCalculatorForm()
    return render(request, 'calc_simple_interest.html', {'form': form})

#--------------------------------------#
# Função para Calcular Juros Compostos
def juros_compostos(principal, taxa_juros, periodo):
    montante = principal * (1 + taxa_juros / 100) ** periodo
    juros = montante - principal
    return round(montante, 2)

# View para a calculadora de juros compostos
@login_required
def calc_compound_interest(request):
    if request.method == 'POST':
        form = CompoundInterestCalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = juros_compostos(principal, taxa_juros, periodo)
            return render(request, 'calc_compound_interest.html', {'form': form, 'montante': montante})
    else:
        form = CompoundInterestCalculatorForm()
    return render(request, 'calc_compound_interest.html', {'form': form})

#--------------------------------------#
# Função para Calcular Investimentos
def calculadora_investimento(valor_inicial, taxa_juros, periodo):
    montante = valor_inicial * (1 + taxa_juros / 100) ** periodo
    return round(montante, 2)

# View para a calculadora de investimento
@login_required
def calc_investment(request):
    if request.method == 'POST':
        form = InvestmentCalculatorForm(request.POST)
        if form.is_valid():
            valor_inicial = form.cleaned_data['valor_inicial']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = calculadora_investimento(valor_inicial, taxa_juros, periodo)
            return render(request, 'calc_investment.html', {'form': form, 'montante': montante})
    else:
        form = InvestmentCalculatorForm()
    return render(request, 'calc_investment.html', {'form': form})

#--------------------------------------#
# Função para Calcular Prestações
def calculadora_prestacoes(montante, taxa_juros, periodo):
    taxa_juros_mensal = taxa_juros / 100 / 12
    num_pagamentos = periodo * 12

    # Calcular o valor da prestação usando a fórmula de amortização de empréstimos
    prestacao = (montante * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_pagamentos)

    return round(prestacao, 2)

# View para a calculadora de prestações
@login_required
def calc_installment(request):
    if request.method == 'POST':
        form = InstallmentCalculatorForm(request.POST)
        if form.is_valid():
            montante = form.cleaned_data['montante']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            prestacao = calculadora_prestacoes(montante, taxa_juros, periodo)
            return render(request, 'calc_installment.html', {'form': form, 'prestacao': prestacao})
    else:
        form = InstallmentCalculatorForm()
    return render(request, 'calc_installment.html', {'form': form})