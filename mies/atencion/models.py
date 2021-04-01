from django.db import models
from empleado.models import Empleado
from inventario.models import InvetarioDistritoCabecera, InventarioTics
# Create your models here.

class TipoDocumento(models.Model):
    """Model definition for TipoDocumento."""

    descripcion = models.CharField('Descripción', max_length=50, unique=True)

    class Meta:
        """Meta definition for TipoDocumento."""

        verbose_name = 'Tipo Documento'
        verbose_name_plural = 'Tipo Documentos'

    def __str__(self):
        """Unicode representation of TipoDocumento."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for TipoDocumento."""
        self.descripcion =(self.descripcion).upper()
        return super(TipoDocumento, self).save(*args, **kwargs)





class Atencion(models.Model):
    """Model definition for Atencion."""

    fechaIncidente = models.DateField('Fecha Incidente', auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    equipo = models.ForeignKey(InvetarioDistritoCabecera, on_delete=models.PROTECT)
    detalle = models.TextField('Detalle', null=True , blank= True)
    hora_ingreso = models.TimeField('Hora Ingreso', auto_now=False, auto_now_add=False)
    hora_salida = models.TimeField('Hora Salida', auto_now=False, auto_now_add=False , null=True , blank= True)
    instalacion =models.BooleanField('Instalación')
    configuracion = models.BooleanField('Configuración')
    prueba = models.BooleanField('Prueba')
    capacitacion = models.BooleanField('Capacitación')
    hardware = models.BooleanField('Hardware')
    software = models.BooleanField('Software')
    observacion = models.TextField('Observación', null=True , blank= True)
    tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    class Meta:
        """Meta definition for Atencion."""

        verbose_name = 'Atención'
        verbose_name_plural = 'Atenciones'

    def __int__(self):
        """Unicode representation of Atencion."""
        return self.fechaIncidente

    def save(self,*args, **kwargs):
        """Save method for Atencion."""
        self.detalle =self.detalle and (self.detalle).upper()
        self.observacion =self.observacion and (self.observacion).upper()
        return super(Atencion, self).save(*args, **kwargs)


class AtencionDetalle(models.Model):
    """Model definition for AtencionDetalle."""
    cabecera = models.ForeignKey(Atencion, on_delete=models.PROTECT)
    pieza = models.ForeignKey(InventarioTics, on_delete=models.PROTECT)
    cantidad = models.IntegerField('Cantidad', default = 1)

    class Meta:
        """Meta definition for AtencionDetalle."""

        verbose_name = 'Atención Detalle'
        verbose_name_plural = 'Atención Detalles'

    def __int__(self):
        """Unicode representation of AtencionDetalle."""
        return self.pieza