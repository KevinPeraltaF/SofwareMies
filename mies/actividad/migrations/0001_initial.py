# Generated by Django 3.2 on 2021-04-26 13:25

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
                ('observacion', models.TextField(verbose_name='Observación')),
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
            name='Prioridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Prioridad')),
            ],
            options={
                'verbose_name': 'Prioridad',
                'verbose_name_plural': 'Prioridades',
            },
        ),
        migrations.CreateModel(
            name='ActividadDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='actividad.asunto')),
                ('cabeceraActividad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='actividad.actividadcabecera')),
            ],
            options={
                'verbose_name': 'Actividad Detalle',
                'verbose_name_plural': 'Actividad Detalles',
            },
        ),
        migrations.AddField(
            model_name='actividadcabecera',
            name='prioridad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='actividad.prioridad'),
        ),
        migrations.AddField(
            model_name='actividadcabecera',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsable_de_actividad', to='empleado.empleado'),
        ),
        migrations.AddField(
            model_name='actividadcabecera',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.area'),
        ),
        migrations.AddField(
            model_name='actividadcabecera',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.empleado'),
        ),
    ]
