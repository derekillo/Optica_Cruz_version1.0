# Generated by Django 4.2.15 on 2024-10-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0003_ordentrabajo_observacionordentrabajo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='apMaternoCliente',
            field=models.CharField(max_length=20, null=True, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='celularCliente',
            field=models.IntegerField(null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='telefonoCliente',
            field=models.IntegerField(null=True, verbose_name='Teléfono'),
        ),
    ]
