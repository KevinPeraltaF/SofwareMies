from django.db import models
from empleado.models import Empleado
from inventario.models import  InventarioTics
from custodio.models import Custodio
from django.utils import timezone
# Create your models here.
from django.db.models import F
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
        try:
            ultimoDocumento = Atencion.objects.all().order_by('contadorDocumento').last()
        
          
            if (self.fechaIncidente.year != ultimoDocumento.fechaIncidente.year):
                self.contadorDocumento =1
            else:
                if self.tipoDocumento == '3'  or self.tipoDocumento == '4':
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

    
    def save(self,*args, **kwargs):
        """Save method for Atencion."""
 
        item = InventarioTics.objects.get(id=self.pieza.id)
        item.cantidad = ( F('cantidad') -self.cantidad)
        item.save()
        return super(AtencionDetalle, self).save(*args, **kwargs)

    



#atencion secundaria--- 

class AtencionSecundaria(models.Model):
    """Model definition for Atencion."""

    fechaIncidente = models.DateField('Fecha Incidente',default=timezone.now)
    responsable = models.ForeignKey(Empleado,verbose_name='Entrega', on_delete=models.PROTECT)
    recibe = models.ForeignKey(Empleado,verbose_name='Recibe', related_name="personaRecibe" ,on_delete=models.PROTECT,null=True )
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

        verbose_name = 'Atención Secundaria'
        verbose_name_plural = 'Atenciones secundaria'

    def __int__(self):
        """Unicode representation of Atencion."""
        return self.fechaIncidente

    def save(self,*args, **kwargs):
        """Save method for Atencion."""
        self.detalle =self.detalle and (self.detalle).upper()
        self.observacion =self.observacion and (self.observacion).upper()
        try:
            ultimoDocumento = Atencion.objects.all().order_by('contadorDocumento').last()
        
          
            if (self.fechaIncidente.year != ultimoDocumento.fechaIncidente.year):
                self.contadorDocumento =1
            else:
                if self.tipoDocumento == '3'  or self.tipoDocumento == '4':
                    self.contadorDocumento =ultimoDocumento.contadorDocumento+1
        except:
            self.contadorDocumento =1

  
        return super(AtencionSecundaria, self).save(*args, **kwargs)


class AtencionSecundariaDetalle(models.Model):
    """Model definition for AtencionDetalle."""
    cabecera = models.ForeignKey(AtencionSecundaria, on_delete=models.CASCADE)
    pieza = models.ForeignKey(InventarioTics, on_delete=models.PROTECT)
    cantidad = models.IntegerField('Cantidad', default = 1)

    class Meta:
        """Meta definition for AtencionDetalle."""

        verbose_name = 'Atención Secundaria Detalle'
        verbose_name_plural = 'Atención Secundaria Detalles'

    def __int__(self):
        """Unicode representation of AtencionDetalle."""
        return self.pieza

    def save(self,*args, **kwargs):
        """Save method for Atencion."""
 
        item = InventarioTics.objects.get(id=self.pieza.id)
        item.cantidad = ( F('cantidad') -self.cantidad)
        item.save()