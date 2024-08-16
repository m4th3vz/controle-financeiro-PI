# calculator/views.py
from django.shortcuts import render
from django.views import View
from .forms import (
    LoanCalculatorForm, 
    SimpleInterestCalculatorForm, 
    CompoundInterestCalculatorForm, 
    InvestmentCalculatorForm, 
    InstallmentCalculatorForm
)

# Página da calculadora
class CalculatorView(View):
    template_name = 'calculator/calculator.html'

    def get(self, request):
        return render(request, self.template_name)

# Página da lista de calculadoras
class CalculatorListView(View):
    template_name = 'calculator/calc_list.html'

    def get(self, request):
        return render(request, self.template_name)

#--------------------------------------#
# Função para Calcular Empréstimo
def calculadora_de_emprestimo(principal, taxa_juros, periodo):
    taxa_juros_mensal = taxa_juros / 100 / 12
    num_pagamentos = periodo * 12

    # Calcular o pagamento mensal de empréstimos
    pagamento_mensal = (principal * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_pagamentos)

    return round(pagamento_mensal, 2)

# View para a calculadora de empréstimo
class LoanCalculatorView(View):
    template_name = 'calculator/calc_loan.html'
    form_class = LoanCalculatorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            pagamento_mensal = calculadora_de_emprestimo(principal, taxa_juros, periodo)
            return render(request, self.template_name, {'form': form, 'pagamento_mensal': pagamento_mensal})
        return render(request, self.template_name, {'form': form})

#--------------------------------------#
# Função para Calcular Juros Simples
def juros_simples(principal, taxa_juros, periodo):
    juros = principal * (taxa_juros / 100) * periodo
    montante = principal + juros
    return round(montante, 2)

# View para a calculadora de juros simples
class SimpleInterestCalculatorView(View):
    template_name = 'calculator/calc_simple_interest.html'
    form_class = SimpleInterestCalculatorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = juros_simples(principal, taxa_juros, periodo)
            return render(request, self.template_name, {'form': form, 'montante': montante})
        return render(request, self.template_name, {'form': form})

#--------------------------------------#
# Função para Calcular Juros Compostos
def juros_compostos(principal, taxa_juros, periodo):
    montante = principal * (1 + taxa_juros / 100) ** periodo
    juros = montante - principal
    return round(montante, 2)

# View para a calculadora de juros compostos
class CompoundInterestCalculatorView(View):
    template_name = 'calculator/calc_compound_interest.html'
    form_class = CompoundInterestCalculatorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = juros_compostos(principal, taxa_juros, periodo)
            return render(request, self.template_name, {'form': form, 'montante': montante})
        return render(request, self.template_name, {'form': form})

#--------------------------------------#
# Função para Calcular Investimentos
def calculadora_investimento(valor_inicial, taxa_juros, periodo):
    montante = valor_inicial * (1 + taxa_juros / 100) ** periodo
    return round(montante, 2)

# View para a calculadora de investimento
class InvestmentCalculatorView(View):
    template_name = 'calculator/calc_investment.html'
    form_class = InvestmentCalculatorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            montante = calculadora_investimento(principal, taxa_juros, periodo)
            return render(request, self.template_name, {'form': form, 'montante': montante})
        return render(request, self.template_name, {'form': form})

#--------------------------------------#
# Função para Calcular Prestações
def calculadora_prestacoes(montante, taxa_juros, periodo):
    taxa_juros_mensal = taxa_juros / 100 / 12
    num_pagamentos = periodo * 12

    # Calcular o valor da prestação usando a fórmula de amortização de empréstimos
    prestacao = (montante * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_pagamentos)

    return round(prestacao, 2)

# View para a calculadora de prestações
class InstallmentCalculatorView(View):
    template_name = 'calculator/calc_installment.html'
    form_class = InstallmentCalculatorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            montante = form.cleaned_data['principal']
            taxa_juros = form.cleaned_data['taxa_juros']
            periodo = form.cleaned_data['periodo']
            prestacao = calculadora_prestacoes(montante, taxa_juros, periodo)
            return render(request, self.template_name, {'form': form, 'prestacao': prestacao})
        return render(request, self.template_name, {'form': form})
