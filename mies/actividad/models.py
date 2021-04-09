from django.db import models
from empleado.models import Area, Empleado
# Create your models here.
class Prioridad(models.Model):
    """Model definition for Prioridad."""

    descripcion = models.CharField('Prioridad', max_length=50, unique =True)

    class Meta:
        """Meta definition for Prioridad."""

        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'

    def __str__(self):
        """Unicode representation of Prioridad."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Prioridad."""
        self.descripcion =(self.descripcion).upper()
        return super(Prioridad, self).save(*args, **kwargs)
        

class Asunto(models.Model):
    """Model definition for Asunto."""

    
    descripcion = models.CharField('Asunto', max_length=50, unique =True)

    class Meta:
        """Meta definition for Asunto."""

        verbose_name = 'Asunto'
        verbose_name_plural = 'Asuntos'

    def __str__(self):
        """Unicode representation of Asunto."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Asunto."""
        self.descripcion =(self.descripcion).upper()
        return super(Asunto, self).save(*args, **kwargs)


class Actividad(models.Model):
    """Model definition for Actividad."""

    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT,related_name='responsable_de_actividad')
    usuario = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    ubicacion = models.ForeignKey(Area, on_delete=models.PROTECT)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.PROTECT)
    observacion = models.TextField('Observación')
    class Meta:
        """Meta definition for Actividad."""

        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades '

    def __int__(self):
        """Unicode representation of Actividad."""
        return self.fecha

 

class ActividadDetalle(models.Model):
    """Model definition for ActividadDetalle."""
    cabeceraActividad = models.ForeignKey(Actividad, on_delete=models.PROTECT)
    asunto =models.ForeignKey(Asunto, on_delete=models.PROTECT)

    class Meta:
        """Meta definition for ActividadDetalle."""

        verbose_name = 'Actividad Detalle'
        verbose_name_plural = 'Actividad Detalles'

    def __int__(self):
        """Unicode representation of ActividadDetalle."""
        return self.asunto
