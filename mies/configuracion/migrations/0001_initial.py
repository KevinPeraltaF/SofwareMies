# Generated by Django 3.2.3 on 2021-05-20 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoIzquierdo', models.ImageField(blank=True, null=True, upload_to='Logos/', verbose_name='Logo izquierdo')),
                ('logocentro', models.ImageField(blank=True, null=True, upload_to='Logos/', verbose_name='Logo centro')),
                ('logoDerecho', models.ImageField(blank=True, null=True, upload_to='Logos/', verbose_name='Logo derecho')),
                ('encargadoBienes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='encargadoBienes', to='empleado.empleado', verbose_name='Encargado Bienes')),
                ('encargadoTics', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.empleado', verbose_name='Encargado Tics')),
            ],
            options={
                'verbose_name': 'Configuracion',
                'verbose_name_plural': 'Configuraciones',
            },
        ),
    ]
