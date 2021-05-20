from django.db import models
from configuracion.models import Configuracion
from inventario.models import  InventarioTics
from custodia.models import Custodia
from django.utils import timezone
# Create your models here.
from django.db.models import F


class Atencion(models.Model):
    
    """Model definition for Atencion."""
    fechaRecepcion = models.DateField('Fecha Recepción',default=timezone.now)
    equipo = models.ManyToManyField(Custodia)


    fechaAtención = models.DateField('Fecha Atención',default=timezone.now)
    fechaEntrega = models.DateField('Fecha Entrega',default=timezone.now)

    
    
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
    contadorDocumento = models.IntegerField(default=0)
    class Meta:
        """Meta definition for Atencion."""

        verbose_name = 'Entrega recepción'
        verbose_name_plural = 'Entrega Recepciones'

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
                self.contadorDocumento =ultimoDocumento.contadorDocumento+1
        except:
            self.contadorDocumento =1

  
        return super(Atencion, self).save(*args, **kwargs)


class AtencionDetalle(models.Model):
    """Model definition for AtencionDetalle."""
    cabecera = models.ForeignKey(Atencion, on_delete=models.CASCADE)
    pieza = models.ForeignKey(InventarioTics, on_delete=models.PROTECT)

    class Meta:
        """Meta definition for AtencionDetalle."""

        verbose_name = 'Atención Detalle'
        verbose_name_plural = 'Atención Detalles'

    def __str__(self):
        """Unicode representation of AtencionDetalle."""
        return str(self.pieza)

    
    def save(self,*args, **kwargs):
        """Save method for Atencion."""
        
        item = InventarioTics.objects.get(id=self.pieza.id)
        item.cantidad = ( F('cantidad') - 1)#siempre sera menos 1
        item.save()
      
        return super(AtencionDetalle, self).save(*args, **kwargs)

    

