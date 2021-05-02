from django.db import models
from empleado.models import Empleado
<<<<<<< HEAD
from inventario.models import InvetarioDistritoCabecera, InventarioTics
from custodio.models import Custodio
=======
from inventario.models import EquipoCabecera, InventarioTics
>>>>>>> a6bb34eff834a94a8898d054ae68c283b9b7de5f
from django.utils import timezone
# Create your models here.


class Atencion(models.Model):
    """Model definition for Atencion."""

    fechaIncidente = models.DateField('Fecha Incidente',default=timezone.now)
<<<<<<< HEAD
    responsable = models.ForeignKey(Empleado,verbose_name='Responsable de Tics', on_delete=models.PROTECT)
    equipo = models.ForeignKey(Custodio, on_delete=models.PROTECT)
=======
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    equipo = models.ForeignKey(EquipoCabecera, on_delete=models.PROTECT)
>>>>>>> a6bb34eff834a94a8898d054ae68c283b9b7de5f
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
    lista_tipoDocumento = [
    ('1', 'REPORTE DE ENTREGA'),
    ('2', 'REPORTE DE RECEPCIÓN'),
    ('3', 'REPORTE DE ENTREGA Y ATENCIÓN'),
    ('4', 'REPORTE ENTREGA A BIENES'),]
    tipoDocumento = models.CharField('Tipo Documento',max_length=1, choices=lista_tipoDocumento, default='1')
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