from django.db import models
from empleado.models import Empleado
from inventario.models import Condicion , InventarioTics
# Create your models here.
class Prestamo(models.Model):
    """Model definition for PrestamoDevolucion."""
    fecha_entrega = models.DateField('Fecha Entrega', auto_now=False, auto_now_add=False)
    fecha_devolucion = models.DateField('Fecha Devolución', auto_now=False, auto_now_add=False, null=True, blank=True)
    usuario = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    item = models.ForeignKey(InventarioTics, on_delete=models.PROTECT,verbose_name='Item')
    cantidad = models.IntegerField('Cantidad',default =1)
    condicion = models.ForeignKey(Condicion, on_delete=models.PROTECT, verbose_name="estado de la  devolución", null=True, blank=True)
    observacion = models.TextField('observación', null = True , blank=True)
    estado = models.BooleanField("Devuelto?")
    class Meta:
        """Meta definition for PrestamoDevolucion."""

        verbose_name = 'Préstamo Devolución'
        verbose_name_plural = 'Prestamos Devoluciones'


    def save(self, *args, **kwargs):
        self.observacion = self.observacion and (self.observacion).upper()
        return super(Prestamo, self).save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of PrestamoDevolucion."""
        return ("{}").format(self.item)


