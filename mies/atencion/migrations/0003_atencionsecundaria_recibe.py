# Generated by Django 3.2.1 on 2021-05-08 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_alter_cargo_descripcion'),
        ('atencion', '0002_atencionsecundaria_atencionsecundariadetalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencionsecundaria',
            name='recibe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='personaRecibe', to='empleado.empleado', verbose_name='Recibe'),
        ),
    ]