# Generated by Django 4.2.15 on 2024-11-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0013_alter_abono_rutcliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='abono',
            name='saldoAnterior',
            field=models.IntegerField(blank=True, null=True, verbose_name='Saldo Anterior'),
        ),
    ]
