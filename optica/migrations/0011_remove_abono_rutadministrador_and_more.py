# Generated by Django 4.2.15 on 2024-11-21 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0010_remove_ordentrabajo_esabono_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abono',
            name='rutAdministrador',
        ),
        migrations.RemoveField(
            model_name='abono',
            name='rutAtendedor',
        ),
        migrations.RemoveField(
            model_name='abono',
            name='rutTecnico',
        ),
    ]
