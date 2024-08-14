# login/urls.py
from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL para login
    path('login/', CustomLoginView.as_view(), name='login'),
    # URL para registro de usuário
    path('register/', views.register, name='register'),
    # URL para logout padrão do Django
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
