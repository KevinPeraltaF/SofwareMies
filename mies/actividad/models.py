from django.db import models
from empleado.models import Area, Empleado
       

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
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Asunto, self).save(*args, **kwargs)


class ActividadCabecera(models.Model):
    """Model definition for ActividadCabecera."""

    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT,related_name='responsable_de_actividad')
    usuario = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    ubicacion = models.ForeignKey(Area, on_delete=models.PROTECT)
    lista_tipo_prioridad = [
    ('1', 'ALTA'),
    ('2', 'MEDIA'),
    ('3', 'BAJA'),]
    prioridad = models.CharField('Prioridad',max_length=1, choices=lista_tipo_prioridad, default='1')

    observacion = models.TextField('Observación', null= True , blank = True)
    class Meta:
        """Meta definition for ActividadCabecera."""

        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades '

    def __int__(self):
        """Unicode representation of ActividadCabecera."""
        return self.fecha

 

class ActividadDetalle(models.Model):
    """Model definition for ActividadDetalle."""
    cabeceraActividad = models.ForeignKey(ActividadCabecera, on_delete=models.CASCADE)
    asunto =models.ForeignKey(Asunto, on_delete=models.PROTECT)

    class Meta:
        """Meta definition for ActividadDetalle."""

        verbose_name = 'Actividad Detalle'
        verbose_name_plural = 'Actividad Detalles'

    def __int__(self):
        """Unicode representation of ActividadDetalle."""
        return self.asunto
