# Generated by Django 4.2.15 on 2024-10-14 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0010_remove_receta_cercaod_remove_receta_cercaoi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='doctorOftalmologo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Médico Oftalmología'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='dvRutCliente',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Dígito'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='rutCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.cliente', verbose_name='RUN'),
        ),
    ]