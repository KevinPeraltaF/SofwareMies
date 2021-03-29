from django.db import models
from datetime import datetime

# Create your models here.
class AccesoRed(models.Model):
    """Model definition for AccesoRed."""

    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False,default=datetime.now())
    usuario = models.CharField('Usuario', max_length=50)
    direccion_mac = models.CharField('Dirección Mac', max_length=50, unique =True, null = True,blank=True)
    direccion_ip = models.CharField('Dirección Ip', max_length=50,unique =True,null = True, blank=True)
    estado = models.BooleanField('Estado', default = True)
    observacion = models.TextField('Observación', null=True, blank=True)

    class Meta:
        """Meta definition for AccesoRed."""

        verbose_name = 'Acceso Red'
        verbose_name_plural = 'Acceso Redes'
    
    def save(self, *args, **kwargs):
        
        self.usuario = (self.usuario).upper()
        self.observacion = (self.observacion).upper()
        self.direccion_ip = self.direccion_ip and (self.direccion_ip).upper()#PARA CAMPOS NO OBLIGATORIOS
        self.direccion_mac = self.direccion_mac and (self.direccion_mac).upper()
        return super(AccesoRed, self).save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of AccesoRed."""
        return self.usuario

 

    