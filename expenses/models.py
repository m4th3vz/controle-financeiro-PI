from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    date = models.DateField(verbose_name='Data')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def __str__(self):
        return self.title
