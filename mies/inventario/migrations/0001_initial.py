# Generated by Django 3.1.7 on 2021-03-26 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapacidadDisco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Capacidad Disco',
                'verbose_name_plural': 'Capacidad Discos',
            },
        ),
        migrations.CreateModel(
            name='CapacidadMemoriaRam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Capacidad Memoria Ram',
                'verbose_name_plural': 'Capacidad Memoria Ram',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Condicion')),
            ],
            options={
                'verbose_name': 'Condicion',
                'verbose_name_plural': 'Condiciones',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Modelo')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
            },
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Procesador',
                'verbose_name_plural': 'Procesadores',
            },
        ),
        migrations.CreateModel(
            name='InvetarioDistritoCabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField(verbose_name='Fecha Ingreso')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción / Nombre')),
                ('serie', models.CharField(blank=True, default='N/A', max_length=50, null=True, unique=True, verbose_name='Serie')),
                ('codigoMies', models.CharField(blank=True, default='N/A', max_length=50, null=True, unique=True, verbose_name='Código Mies')),
                ('direccionIp', models.CharField(blank=True, default='N/A', max_length=50, null=True, unique=True, verbose_name='Dirección Ip')),
                ('direccionMac', models.CharField(blank=True, default='N/A', max_length=50, null=True, unique=True, verbose_name='Dirección Mac Address')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='InventarioDistrito/%Y/%m/%d/', verbose_name='Foto')),
                ('capacidadDisco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.capacidaddisco')),
                ('capacidadMemoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.capacidadmemoriaram')),
                ('capacidadProcesador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.procesador')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria')),
                ('condicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.condicion')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.modelo')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.area')),
            ],
            options={
                'verbose_name': 'Invetario Distrito ',
                'verbose_name_plural': 'Invetario Distrito ',
            },
        ),
        migrations.CreateModel(
            name='InventarioTics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField(verbose_name='Fecha Ingreso')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción / Nombre')),
                ('serie', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Serie')),
                ('codigoMies', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Código Mies')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='InventarioTics/%Y/%m/%d/', verbose_name='Foto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria')),
                ('condicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.condicion')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.modelo')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.area')),
            ],
            options={
                'verbose_name': 'Inventario Tics',
                'verbose_name_plural': 'Inventario Tics',
            },
        ),
        migrations.CreateModel(
            name='InventarioDistritoDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('cabeceraDistrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.invetariodistritocabecera')),
                ('periferico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.inventariotics')),
            ],
            options={
                'verbose_name': 'Inventario Distrito Detalle',
                'verbose_name_plural': 'Inventario Distrito Detalles',
            },
        ),
    ]