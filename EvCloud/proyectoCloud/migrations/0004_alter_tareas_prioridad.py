# Generated by Django 5.0.6 on 2024-06-08 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoCloud', '0003_tareasfinalizadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='prioridad',
            field=models.CharField(choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=5),
        ),
    ]
