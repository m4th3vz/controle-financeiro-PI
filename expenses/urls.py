from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/', views.confirm_delete_expenses, name='confirm_delete_expenses'),
    path('delete/all/', views.delete_all_expenses, name='delete_all_expenses'),
    path('<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
    path('calculator/', views.calculator, name='calculator'),
]
