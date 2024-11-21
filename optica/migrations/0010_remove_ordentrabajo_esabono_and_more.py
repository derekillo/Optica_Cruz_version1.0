# Generated by Django 4.2.15 on 2024-11-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0009_remove_ordentrabajo_espagototal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordentrabajo',
            name='esAbono',
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='estadoDelPago',
            field=models.CharField(default=11, max_length=20, verbose_name='Estado del Pago'),
            preserve_default=False,
        ),
    ]
