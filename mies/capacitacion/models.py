from django.db import models
from empleado.models import Empleado
# Create your models here.

class CapacitacionCabecera(models.Model):
    """Model definition for CapacitacionCabecera."""
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    hora_inicio = models.TimeField('Hora Inicio', auto_now=False, auto_now_add=False)
    hora_fin = models.TimeField('Hora Fin', auto_now=False, auto_now_add=False)
    lugar = models.CharField('Lugar', max_length=80)
    tema = models.CharField('Tema', max_length=80)
    lista_tipo_capacitacion = [
    ('1', 'PRESENCIAL'),
    ('2', 'VIDEO CONFERENCIA'),
    ('3', 'SKYPE'),
    ('4', 'TELEFÓNICA'),]
    tipoCapacitacion = models.CharField('Tipo Capacitación',max_length=1, choices=lista_tipo_capacitacion, default='1')
    areaSolicitante = models.CharField('Area Solicitante', max_length=80)
    dirigido = models.CharField('Dirigido a', max_length=80)
    instructor = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    objetivo = models.TextField('Objetivo')
    class Meta:
        """Meta definition for CapacitacionCabecera."""

        verbose_name = 'Capacitacion'
        verbose_name_plural = 'Capacitaciones'

    def __str__(self):
        """Unicode representation of CapacitacionCabecera."""
        return self.tema

    def save(self,*args, **kwargs):
        """Save method for CapacitacionCabecera."""
        self.lugar =self.lugar and (self.lugar).upper()
        self.tema = self.tema and (self.tema).upper()
        self.areaSolicitante =self.areaSolicitante and (self.areaSolicitante).upper()
        self.dirigido = self.dirigido and (self.dirigido).upper()
        self.objetivo = self.objetivo and (self.objetivo).upper()
        return super(CapacitacionCabecera, self).save(*args, **kwargs)




class CapacitacionDetalle(models.Model):
    """Model definition for CapacitacionDetalle."""
    capacitacionCabecera = models.ForeignKey(CapacitacionCabecera, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, null=True,blank=True)
    observacion = models.CharField('observación', max_length=100, null= True, blank=True)

    class Meta:
        """Meta definition for CapacitacionDetalle."""

        verbose_name = 'Capacitacion Detalle'
        verbose_name_plural = 'Capacitacion Detalles'

    def __int__(self):
        """Unicode representation of CapacitacionDetalle."""
        return self.empleado


