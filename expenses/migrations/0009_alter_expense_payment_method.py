# Generated by Django 5.0.3 on 2024-04-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_expense_duration_months_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Dinheiro', 'Dinheiro'), ('Crédito', 'Crédito'), ('Débito', 'Débito'), ('Pix', 'Pix'), ('Boleto', 'Boleto'), ('Voucher', 'Voucher'), ('Crediário', 'Crediário'), ('Transferência', 'Transferência'), ('Cartão de loja', 'Cartão de loja')], default='Dinheiro', max_length=20, verbose_name='Forma de Pagamento (Opcional)'),
        ),
    ]
