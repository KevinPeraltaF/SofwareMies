# Generated by Django 3.2 on 2021-05-02 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20210424_1251'),
        ('custodio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custodio',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.equipocabecera'),
        ),
    ]
