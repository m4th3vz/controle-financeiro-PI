# calculator/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL para a calculadora
    path('calculator/', views.calculator, name='calculator'),
    # URL para a lista de calculadoras
    path('calculator_list/', views.calc_list, name='calc_list'),
    # URL para página da calculadora de empréstimo
    path('loan-calculator/', views.calc_loan, name='calc_loan'),
    # URL para página da calculadora juros simples
    path('simple-interest-calculator/', views.calc_simple_interest, name='calc_simple_interest'),
    # URL para página da calculadora juros compostos
    path('compound-interest-calculator/', views.calc_compound_interest, name='calc_compound_interest'),
    # URL para página da calculadora de investimentos
    path('investment-calculator/', views.calc_investment, name='calc_investment'),
    # URL para página da calculadora de prestações
    path('installment-calculator/', views.calc_installment, name='calc_installment'),
]
