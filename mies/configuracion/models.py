from django.db import models
from empleado.models import Empleado
# Create your models here.
class Configuracion(models.Model):
    """Model definition for Configuracion."""

    EncargadoBienes = models.ForeignKey(Empleado,verbose_name='Responsable de Tics', on_delete=models.PROTECT)
    logoDerecho = models.ImageField('logo Derecho', upload_to='Logo/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    logoMedio = models.ImageField('logo Medio', upload_to='Logo/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    logoIzquierdo = models.ImageField('logo Izquierdo', upload_to='Logo/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    class Meta:
        """Meta definition for Configuracion."""

        verbose_name = 'Configuracion'
        verbose_name_plural = 'Configuraciones'

    def __str__(self):
        """Unicode representation of Configuracion."""
        pass
