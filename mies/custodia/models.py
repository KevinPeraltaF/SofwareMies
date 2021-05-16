from django.db import models
from django.utils import timezone
from empleado.models import Empleado
from inventario.models import Dispositivo
# Create your models here.
class Custodia(models.Model):
    """Model definition for AccesoRed."""

    fecha = models.DateField('Fecha',default=timezone.now)
    custodio = models.ForeignKey(Empleado,verbose_name='Custodio a asignar:', on_delete=models.PROTECT)
    equipo = models.ForeignKey(Dispositivo, on_delete=models.PROTECT)
    custodioAnterior = models.ForeignKey(Empleado,verbose_name='Custodio Anterior',related_name="custodioAnterior", on_delete=models.PROTECT,  null= True, blank=True)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        """Meta definition for AccesoRed."""

        verbose_name = 'Asignar Custodio'
        verbose_name_plural = 'Asignar Custodios'

    def __str__(self):
        """Unicode representation of AccesoRed."""
        return ("{} {}- {}").format(self.custodio.apellidos, self.custodio.nombres)

    def save(self, *args, **kwargs):
        
        try:
            #cambio el estado a no vigente. al equipo que se este creando 
            equipo =  Custodia.objects.filter(equipo=self.equipo.id, estado=1).update(estado=0)
        except:
            pass
        return super(Custodia, self).save(*args, **kwargs)
 