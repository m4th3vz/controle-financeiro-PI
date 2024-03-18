from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL para listar as despesas
    path('', views.expense_list, name='expense_list'),
    # URL para adicionar uma nova despesa
    path('add/', views.add_expense, name='add_expense'),
    # URL para confirmar a exclusão de todas as despesas
    path('delete/', views.confirm_delete_expenses, name='confirm_delete_expenses'),
    # URL para excluir todas as despesas
    path('delete/all/', views.delete_all_expenses, name='delete_all_expenses'),
    # URL para excluir uma despesa específica
    path('<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
    # URL para a calculadora
    path('calculator/', views.calculator, name='calculator'),
    # URL para login personalizado
    path('login/', CustomLoginView.as_view(), name='login'),
    # URL para registro de usuário
    path('register/', views.register, name='register'),
    # URL para logout padrão do Django
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # URL para página de boas-vindas
    path('welcome/', views.welcome, name='welcome'),
]
