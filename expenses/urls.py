# expenses/urls.py
from django.urls import path
from .views import ExpenseListView, AddExpenseView, DeleteExpenseView, DeleteAllExpensesView, ConfirmDeleteExpensesView

urlpatterns = [
    # URL para listar as despesas
    path('expenses/', ExpenseListView.as_view(), name='expense_list'),
    # URL para listar despesas por ano e mês
    path('expenses/<int:year>/<int:month>/', ExpenseListView.as_view(), name='expense_list_month'),
    # URL para adicionar uma nova despesa
    path('add/', AddExpenseView.as_view(), name='add_expense'),
    # URL para confirmar a exclusão de todas as despesas
    path('delete/', ConfirmDeleteExpensesView.as_view(), name='confirm_delete_expenses'),
    # URL para excluir todas as despesas
    path('delete/all/', DeleteAllExpensesView.as_view(), name='delete_all_expenses'),
    # URL para excluir uma despesa específica
    path('<int:expense_id>/delete/', DeleteExpenseView.as_view(), name='delete_expense'),
]
