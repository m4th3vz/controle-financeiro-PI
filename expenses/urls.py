# expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL para listar as despesas
    path('expenses/', views.expense_list, name='expense_list'),
    # URL para adicionar uma nova despesa
    path('add/', views.add_expense, name='add_expense'),
    # URL para confirmar a exclusão de todas as despesas
    path('delete/', views.confirm_delete_expenses, name='confirm_delete_expenses'),
    # URL para excluir todas as despesas
    path('delete/all/', views.delete_all_expenses, name='delete_all_expenses'),
    # URL para excluir uma despesa específica
    path('<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
    # URL dinâmica
    path('expenses/<int:year>/<int:month>/', views.expense_list, name='expense_list_month'),
]
