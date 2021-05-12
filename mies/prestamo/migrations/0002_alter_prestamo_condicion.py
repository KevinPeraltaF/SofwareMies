# Generated by Django 3.2.1 on 2021-05-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='condicion',
            field=models.CharField(choices=[('1', 'BUENO'), ('2', 'DAÑADO')], default='1', max_length=1, verbose_name='estado de la  devolución'),
        ),
    ]