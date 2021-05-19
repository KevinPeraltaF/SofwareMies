from django.db import models
from empleado.models import Empleado
# Create your models here.
class Configuracion(models.Model):
    """Model definition for Configuracion."""

    encargadoTics = models.ForeignKey(Empleado,verbose_name='Encargado Tics', on_delete=models.PROTECT)
    encargadoBienes = models.ForeignKey(Empleado,related_name="encargadoBienes",verbose_name='Encargado Bienes', on_delete=models.PROTECT)
    logoIzquierdo = models.ImageField('Logo izquierdo', upload_to='Logos/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    logocentro = models.ImageField('Logo centro', upload_to='Logos/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    logoDerecho = models.ImageField('Logo derecho', upload_to='Logos/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for Configuracion."""

        verbose_name = 'Configuracion'
        verbose_name_plural = 'Configuraciones'

    def __str__(self):
        """Unicode representation of Configuracion."""
        return str(self.encargadoTics)


