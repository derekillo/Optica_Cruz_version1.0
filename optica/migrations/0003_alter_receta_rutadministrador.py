# Generated by Django 4.2.15 on 2024-10-19 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0002_alter_receta_rutadministrador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='rutAdministrador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='optica.administrador', verbose_name='RUN Administrador'),
        ),
    ]
