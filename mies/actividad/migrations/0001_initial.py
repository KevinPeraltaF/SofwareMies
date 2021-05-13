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
            name='ActividadCabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('prioridad', models.CharField(choices=[('1', 'ALTA'), ('2', 'MEDIA'), ('3', 'BAJA')], default='1', max_length=1, verbose_name='Prioridad')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observación')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsable_de_actividad', to='empleado.empleado')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.area', verbose_name='Ubicación')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.empleado')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades ',
            },
        ),
        migrations.CreateModel(
            name='Asunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Asunto')),
            ],
            options={
                'verbose_name': 'Asunto',
                'verbose_name_plural': 'Asuntos',
            },
        ),
        migrations.CreateModel(
            name='ActividadDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='actividad.asunto')),
                ('cabeceraActividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividad.actividadcabecera')),
            ],
            options={
                'verbose_name': 'Actividad Detalle',
                'verbose_name_plural': 'Actividad Detalles',
            },
        ),
    ]
