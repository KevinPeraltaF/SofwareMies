# Generated by Django 3.1.7 on 2021-04-04 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0004_auto_20210403_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atenciondetalle',
            name='cabecera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.atencion'),
        ),
    ]
