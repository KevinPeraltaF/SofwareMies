# Generated by Django 3.2 on 2021-04-16 15:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIncidente', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Incidente')),
                ('detalle', models.TextField(blank=True, null=True, verbose_name='Detalle')),
                ('fecha_salida', models.DateField(verbose_name='Fecha Salida')),
                ('hora_salida', models.TimeField(verbose_name='Hora Salida')),
                ('instalacion', models.BooleanField(verbose_name='Instalación')),
                ('configuracion', models.BooleanField(verbose_name='Configuración')),
                ('prueba', models.BooleanField(verbose_name='Prueba')),
                ('capacitacion', models.BooleanField(verbose_name='Capacitación')),
                ('hardware', models.BooleanField(verbose_name='Hardware')),
                ('software', models.BooleanField(verbose_name='Software')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observación')),
                ('contadorDocumento', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Atención',
                'verbose_name_plural': 'Atenciones',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo Documento',
                'verbose_name_plural': 'Tipo Documentos',
            },
        ),
        migrations.CreateModel(
            name='AtencionDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('cabecera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.atencion')),
            ],
            options={
                'verbose_name': 'Atención Detalle',
                'verbose_name_plural': 'Atención Detalles',
            },
        ),
    ]
