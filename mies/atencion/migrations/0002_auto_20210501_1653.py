# Generated by Django 3.2 on 2021-05-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='tipoDocumento',
            field=models.CharField(choices=[('1', 'REPORTE DE ENTREGA'), ('2', 'REPORTE DE RECEPCIÓN'), ('3', 'REPORTE DE ENTREGA Y ATENCIÓN'), ('4', 'REPORTE ENTREGA A BIENES')], default='1', max_length=1, verbose_name='Tipo Documento'),
        ),
        migrations.DeleteModel(
            name='TipoDocumento',
        ),
    ]
