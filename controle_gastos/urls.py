from django.contrib import admin
from django.urls import path, include
from expenses.views import add_expense, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('add/', add_expense, name='add_expense'),
    path('admin/', admin.site.urls),
    path('', include('expenses.urls')),
]
