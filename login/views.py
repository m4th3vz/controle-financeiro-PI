# login/views.py
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# Personalização da página de login
class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('welcome')
    
# Página de registro de usuário
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Adiciona mensagens de erro ao contexto
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'login/register.html', {'form': form})
