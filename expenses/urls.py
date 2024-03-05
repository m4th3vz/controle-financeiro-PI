from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/', views.confirm_delete_expenses, name='confirm_delete_expenses'),
    path('delete/all/', views.delete_all_expenses, name='delete_all_expenses'),
    path('<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
    path('calculator/', views.calculator, name='calculator'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
