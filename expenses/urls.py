# expenses/urls.py
from django.urls import path
from .views import ExpenseListView, AddExpenseView, DeleteExpenseView, ConfirmDeleteExpensesView

urlpatterns = [
    path('expenses/', ExpenseListView.as_view(), name='expense_list'),
    path('expenses/<int:year>/<int:month>/', ExpenseListView.as_view(), name='expense_list_month'),
    path('add/', AddExpenseView.as_view(), name='add_expense'),
    path('delete/', ConfirmDeleteExpensesView.as_view(), name='confirm_delete_expenses'),
    path('delete/all/', ConfirmDeleteExpensesView.as_view(), name='delete_all_expenses'),
    path('expenses/<int:expense_id>/delete/', DeleteExpenseView.as_view(), name='delete_expense'),
]
