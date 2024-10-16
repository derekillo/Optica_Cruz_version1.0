# Generated by Django 4.2.15 on 2024-10-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0009_alter_receta_imagenreceta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='cercaOd',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='cercaOi',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='lejosOd',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='lejosOi',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='linkFotoReceta',
        ),
        migrations.AddField(
            model_name='receta',
            name='cercaOdCilindro',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cilindro'),
        ),
        migrations.AddField(
            model_name='receta',
            name='cercaOdEje',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Eje'),
        ),
        migrations.AddField(
            model_name='receta',
            name='cercaOdEsfera',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Esfera'),
        ),
        migrations.AddField(
            model_name='receta',
            name='cercaOiCilindro',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cilindro'),
        ),
        migrations.AddField(
            model_name='receta',
            name='cercaOiEje',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Eje'),
        ),
        migrations.AddField(
            model_name='receta',
            name='cercaOiEsfera',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Esfera'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lejosOdCilindro',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cilindro'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lejosOdEje',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Eje'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lejosOdEsfera',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Esfera'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lejosOiCilindro',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cilindro'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lejosOiEje',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Eje'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lejosOiEsfera',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Esfera'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='doctorOftalmologo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Tecnologo(a) Oftalmologia'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='dpCerca',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Distancia Pupilar'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='dpLejos',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Distancia Pupilar'),
        ),
    ]
