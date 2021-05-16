# Generated by Django 3.2.1 on 2021-05-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practica', '0002_alter_pasante_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasante',
            name='estado',
            field=models.CharField(choices=[('1', 'EN FUNCIONES'), ('2', 'SOLICITADO'), ('3', 'FINALIZADO')], default='1', max_length=1, verbose_name='Estado'),
        ),
    ]