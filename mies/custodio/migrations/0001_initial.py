# Generated by Django 3.2 on 2021-05-01 22:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('custodio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.empleado', verbose_name='Empleado Custodio')),
                ('custodioAnterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='custodioAnterior', to='empleado.empleado', verbose_name='Custodio Anterior')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.invetariodistritocabecera')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.area', verbose_name='Ubicación')),
            ],
            options={
                'verbose_name': 'Asignar Custodio',
                'verbose_name_plural': 'Asignar Custodios',
            },
        ),
    ]
