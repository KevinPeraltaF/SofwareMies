# Generated by Django 3.1.7 on 2021-04-04 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_auto_20210402_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventariodistritodetalle',
            name='cabeceraDistrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='inventario.invetariodistritocabecera'),
        ),
    ]
