# Generated by Django 5.0.6 on 2024-11-10 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
