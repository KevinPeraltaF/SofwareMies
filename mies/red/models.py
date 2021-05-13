from django.db import models
from django.utils import timezone

# Create your models here.
class AccesoRed(models.Model):
    """Model definition for AccesoRed."""
    usuario = models.CharField('Usuario', max_length=50)
    direccion_mac = models.CharField('Dirección Mac', max_length=50, unique =True, null = True,blank=True)
    direccion_ip = models.CharField('Dirección Ip', max_length=50,unique =True,null = True, blank=True)
    estado = models.BooleanField('Está conectado?', default = True)
    observacion = models.TextField('Observación', null=True, blank=True)

    class Meta:
        """Meta definition for AccesoRed."""

        verbose_name = 'Acceso Red'
        verbose_name_plural = 'Acceso Redes'
    
    def save(self, *args, **kwargs):
        
        self.usuario = self.usuario and (self.usuario).upper()
        self.observacion = self.observacion and (self.observacion).upper()
        self.direccion_ip = self.direccion_ip and (self.direccion_ip).upper()#PARA CAMPOS NO OBLIGATORIOS
        self.direccion_mac = self.direccion_mac and (self.direccion_mac).upper()
        return super(AccesoRed, self).save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of AccesoRed."""
        return self.usuario

 

    