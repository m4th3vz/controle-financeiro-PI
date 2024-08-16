# login/urls.py
from django.urls import path
from .views import CustomLoginView, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL para login
    path('login/', CustomLoginView.as_view(), name='login'),
    # URL para registro de usuário
    path('register/', RegisterView.as_view(), name='register'),
    # URL para logout padrão do Django
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
