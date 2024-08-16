# calculator/urls.py
from django.urls import path
from .views import (
    CalculatorView, 
    CalculatorListView, 
    LoanCalculatorView, 
    SimpleInterestCalculatorView, 
    CompoundInterestCalculatorView, 
    InvestmentCalculatorView, 
    InstallmentCalculatorView
)

urlpatterns = [
    # URL para a calculadora
    path('calculator/', CalculatorView.as_view(), name='calculator'),
    # URL para a lista de calculadoras
    path('calculator_list/', CalculatorListView.as_view(), name='calc_list'),
    # URL para página da calculadora de empréstimo
    path('loan-calculator/', LoanCalculatorView.as_view(), name='calc_loan'),
    # URL para página da calculadora de juros simples
    path('simple-interest-calculator/', SimpleInterestCalculatorView.as_view(), name='calc_simple_interest'),
    # URL para página da calculadora de juros compostos
    path('compound-interest-calculator/', CompoundInterestCalculatorView.as_view(), name='calc_compound_interest'),
    # URL para página da calculadora de investimentos
    path('investment-calculator/', InvestmentCalculatorView.as_view(), name='calc_investment'),
    # URL para página da calculadora de prestações
    path('installment-calculator/', InstallmentCalculatorView.as_view(), name='calc_installment'),
]
