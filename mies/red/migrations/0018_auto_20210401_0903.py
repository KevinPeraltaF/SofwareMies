# Generated by Django 3.1.7 on 2021-04-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0017_merge_20210401_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesored',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
    ]