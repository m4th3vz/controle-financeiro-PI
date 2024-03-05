from django.contrib import admin
from django.urls import path, include
from expenses.views import expense_list, add_expense

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    path('admin/', admin.site.urls),
    path('', include('expenses.urls')),
]
