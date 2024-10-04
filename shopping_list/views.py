# shopping_list/views.py
from django.views import View
from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'shopping_list/task_list.html', {'tasks': tasks})

class TaskCreateView(LoginRequiredMixin, View):
    def post(self, request):
        title = request.POST.get('title')
        if title:
            if len(title) > 30:
                messages.error(request, "O título não pode ter mais de 30 caracteres.")
            else:
                Task.objects.create(title=title, user=request.user)
        return redirect('task_list')

class TaskDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = Task.objects.filter(pk=pk, user=request.user).first()
        if task:
            task.delete()
        return redirect('task_list')
