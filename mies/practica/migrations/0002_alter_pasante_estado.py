# Generated by Django 3.2.1 on 2021-05-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasante',
            name='estado',
            field=models.BooleanField(verbose_name='Prácticas profesionales finalizadas?'),
        ),
    ]
