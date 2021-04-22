from django.db import models
from empleado.models import Empleado
from inventario.models import InvetarioDistritoCabecera, InventarioTics
from custodio.models import Custodio
from django.utils import timezone
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

    fechaIncidente = models.DateField('Fecha Incidente',default=timezone.now)
    responsable = models.ForeignKey(Empleado,verbose_name='Responsable de Tics', on_delete=models.PROTECT)
    equipo = models.ForeignKey(Custodio, on_delete=models.PROTECT)
    detalle = models.TextField('Detalle', null=True , blank= True)
    fecha_salida = models.DateField('Fecha Salida', auto_now=False, auto_now_add=False, null=True , blank= True)
    hora_salida = models.TimeField('Hora Salida', null=True , blank= True)
    instalacion =models.BooleanField('Instalación')
    configuracion = models.BooleanField('Configuración')
    prueba = models.BooleanField('Prueba')
    capacitacion = models.BooleanField('Capacitación')
    hardware = models.BooleanField('Hardware')
    software = models.BooleanField('Software')
    observacion = models.TextField('Observación', null=True , blank= True)
    tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    contadorDocumento = models.IntegerField(default=0)
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
        print('entro')
        #ultimoDocumento = Atencion.objects.all().order_by('contadorDocumento').last()
        try:
            ultimoDocumento = Atencion.objects.all().order_by('contadorDocumento').last()
        
          
            if (self.fechaIncidente.year != ultimoDocumento.fechaIncidente.year):
                self.contadorDocumento =1
            else:
                if self.tipoDocumento.id == 3  or self.tipoDocumento.id == 4:
                    self.contadorDocumento =ultimoDocumento.contadorDocumento+1
        except:
            self.contadorDocumento =1

  
        return super(Atencion, self).save(*args, **kwargs)


class AtencionDetalle(models.Model):
    """Model definition for AtencionDetalle."""
    cabecera = models.ForeignKey(Atencion, on_delete=models.CASCADE)
    pieza = models.ForeignKey(InventarioTics, on_delete=models.PROTECT)
    cantidad = models.IntegerField('Cantidad', default = 1)

    class Meta:
        """Meta definition for AtencionDetalle."""

        verbose_name = 'Atención Detalle'
        verbose_name_plural = 'Atención Detalles'

    def __int__(self):
        """Unicode representation of AtencionDetalle."""
        return self.pieza