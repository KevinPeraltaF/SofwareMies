# Generated by Django 3.2 on 2021-04-13 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_merge_20210405_0838'),
        ('actividad', '0004_auto_20210401_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadcabecera',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsable_de_actividad', to='empleado.empleado'),
        ),
    ]
