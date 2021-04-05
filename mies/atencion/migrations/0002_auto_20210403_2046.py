# Generated by Django 3.1.7 on 2021-04-04 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='fechaIncidente',
            field=models.DateField(verbose_name='Fecha Incidente'),
        ),
        migrations.AlterField(
            model_name='atenciondetalle',
            name='cabecera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='atencion.atencion'),
        ),
    ]