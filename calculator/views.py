# calculator/views.py
from .forms import LoanCalculatorForm, SimpleInterestCalculatorForm, CompoundInterestCalculatorForm, InvestmentCalculatorForm, InstallmentCalculatorForm
from django.shortcuts import render

# Página da calculadora
def calculator(request):
    return render(request, 'calculator/calculator.html')

# Página da lista de calculadoras
def calc_list(request):
    return render(request, 'calculator/calc_list.html')

#--------------------------------------#
# Função para Calcular Empréstimo
def calculadora_de_emprestimo(principal, taxa_juros, periodo):
    taxa_juros_mensal = taxa_juros / 100 / 12
    num_pagamentos = periodo * 12

    # Calcular o pagamento mensal de empréstimos
    pagamento_mensal = (principal * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_pagamentos)

    return round(pagamento_mensal, 2)

# Esta view é uma aplicação Django e coordena a interação do usuário com a interface web
def calc_loan(request):
    if request.method == 'POST':
        form = LoanCalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            pagamento_mensal = calculadora_de_emprestimo(principal, taxa_juros, periodo)
            return render(request, 'calculator/calc_loan.html', {'form': form, 'pagamento_mensal': pagamento_mensal})
    else:
        form = LoanCalculatorForm()
    return render(request, 'calculator/calc_loan.html', {'form': form})

#--------------------------------------#
# Função para Calcular Juros Simples
def juros_simples(principal, taxa_juros, periodo):
    juros = principal * (taxa_juros / 100) * periodo
    montante = principal + juros
    return round(montante, 2)

# View para a calculadora de juros simples
def calc_simple_interest(request):
    if request.method == 'POST':
        form = SimpleInterestCalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = juros_simples(principal, taxa_juros, periodo)
            return render(request, 'calculator/calc_simple_interest.html', {'form': form, 'montante': montante})
    else:
        form = SimpleInterestCalculatorForm()
    return render(request, 'calculator/calc_simple_interest.html', {'form': form})

#--------------------------------------#
# Função para Calcular Juros Compostos
def juros_compostos(principal, taxa_juros, periodo):
    montante = principal * (1 + taxa_juros / 100) ** periodo
    juros = montante - principal
    return round(montante, 2)

# View para a calculadora de juros compostos
def calc_compound_interest(request):
    if request.method == 'POST':
        form = CompoundInterestCalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = juros_compostos(principal, taxa_juros, periodo)
            return render(request, 'calculator/calc_compound_interest.html', {'form': form, 'montante': montante})
    else:
        form = CompoundInterestCalculatorForm()
    return render(request, 'calculator/calc_compound_interest.html', {'form': form})

#--------------------------------------#
# Função para Calcular Investimentos
def calculadora_investimento(valor_inicial, taxa_juros, periodo):
    montante = valor_inicial * (1 + taxa_juros / 100) ** periodo
    return round(montante, 2)

# View para a calculadora de investimento
def calc_investment(request):
    if request.method == 'POST':
        form = InvestmentCalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = calculadora_investimento(principal, taxa_juros, periodo)
            return render(request, 'calculator/calc_investment.html', {'form': form, 'montante': montante})
    else:
        form = InvestmentCalculatorForm()
    return render(request, 'calculator/calc_investment.html', {'form': form})

#--------------------------------------#
# Função para Calcular Prestações
def calculadora_prestacoes(montante, taxa_juros, periodo):
    taxa_juros_mensal = taxa_juros / 100 / 12
    num_pagamentos = periodo * 12

    # Calcular o valor da prestação usando a fórmula de amortização de empréstimos
    prestacao = (montante * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_pagamentos)

    return round(prestacao, 2)

# View para a calculadora de prestações
def calc_installment(request):
    if request.method == 'POST':
        form = InstallmentCalculatorForm(request.POST)
        if form.is_valid():
            montante = form.cleaned_data['principal']  # Renomeie 'montante' para 'principal'
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            prestacao = calculadora_prestacoes(montante, taxa_juros, periodo)
            return render(request, 'calculator/calc_installment.html', {'form': form, 'prestacao': prestacao})
    else:
        form = InstallmentCalculatorForm()
    return render(request, 'calculator/calc_installment.html', {'form': form})
