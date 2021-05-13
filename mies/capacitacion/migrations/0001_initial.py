# Generated by Django 3.2.1 on 2021-05-13 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapacitacionCabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora_inicio', models.TimeField(verbose_name='Hora Inicio')),
                ('hora_fin', models.TimeField(verbose_name='Hora Fin')),
                ('lugar', models.CharField(max_length=80, verbose_name='Lugar')),
                ('tema', models.CharField(max_length=80, verbose_name='Tema')),
                ('tipoCapacitacion', models.CharField(choices=[('1', 'PRESENCIAL'), ('2', 'VIDEO CONFERENCIA'), ('3', 'SKYPE'), ('4', 'TELEFÓNICA')], default='1', max_length=1, verbose_name='Tipo Capacitación')),
                ('dirigido', models.CharField(max_length=80, verbose_name='Dirigido a')),
                ('objetivo', models.TextField(verbose_name='Objetivo')),
                ('areaSolicitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.area')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.empleado')),
            ],
            options={
                'verbose_name': 'Capacitacion',
                'verbose_name_plural': 'Capacitaciones',
            },
        ),
        migrations.CreateModel(
            name='CapacitacionDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='observación')),
                ('capacitacionCabecera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capacitacion.capacitacioncabecera')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empleado.empleado')),
            ],
            options={
                'verbose_name': 'Capacitacion Detalle',
                'verbose_name_plural': 'Capacitacion Detalles',
            },
        ),
    ]
