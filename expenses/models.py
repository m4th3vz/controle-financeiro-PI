from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=100, verbose_name='título')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='valor')
    date = models.DateField(verbose_name='data')

    class Meta:
        verbose_name = 'despesa'
        verbose_name_plural = 'despesas'

    def __str__(self):
        return self.title
