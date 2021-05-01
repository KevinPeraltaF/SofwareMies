# Generated by Django 3.2 on 2021-05-01 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
        ('custodio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custodio',
            name='custodioAnterior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='custodioAnterior', to='empleado.empleado', verbose_name='Empleado Anterior'),
        ),
    ]
