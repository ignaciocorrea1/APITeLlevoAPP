# Generated by Django 5.0.6 on 2024-11-27 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudviaje',
            name='pasajero',
        ),
        migrations.RemoveField(
            model_name='solicitudviaje',
            name='viaje',
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='conductor',
        ),
        migrations.DeleteModel(
            name='DetalleViaje',
        ),
        migrations.DeleteModel(
            name='SolicitudViaje',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Viaje',
        ),
    ]