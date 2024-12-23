# Generated by Django 5.0.6 on 2024-11-10 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0007_remove_usuario_tipo_delete_tipousuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=80)),
                ('paterno', models.CharField(max_length=30)),
                ('materno', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('contrasenia', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('idViaje', models.AutoField(db_column='idViaje', primary_key=True, serialize=False)),
                ('costoPersona', models.IntegerField()),
                ('capacidadActual', models.IntegerField(default=0)),
                ('capacidadMaxima', models.IntegerField()),
                ('direccionInicio', models.CharField(max_length=50)),
                ('direccionFinal', models.CharField(max_length=50)),
                ('horaInicio', models.TimeField()),
                ('conductor', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudViaje',
            fields=[
                ('idSolicitud', models.AutoField(db_column='idSolicitud', primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=30)),
                ('pasajero', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
                ('viaje', models.ForeignKey(db_column='idViaje', on_delete=django.db.models.deletion.CASCADE, to='api.viaje')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleViaje',
            fields=[
                ('idDetalle', models.AutoField(db_column='idDetalle', primary_key=True, serialize=False)),
                ('pasajero', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
                ('idViaje', models.ForeignKey(db_column='idViaje', on_delete=django.db.models.deletion.CASCADE, to='api.viaje')),
            ],
        ),
    ]
