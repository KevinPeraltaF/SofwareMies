# Generated by Django 3.2 on 2021-05-01 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Zona')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Provincia')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ubicacion.zona')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Distrito')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ubicacion.provincia')),
            ],
            options={
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
            },
        ),
    ]
