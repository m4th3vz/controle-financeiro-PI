# login/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .forms import UserRegistrationForm

# Personalização da página de login
class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('welcome')

# Página de registro de usuário baseada em classe
class RegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'login/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Adiciona mensagens de erro ao contexto
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        return render(request, self.template_name, {'form': form})
