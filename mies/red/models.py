from django.db import models

# Create your models here.
class AccesoRed(models.Model):
    """Model definition for AccesoRed."""

    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    usuario = models.CharField('Usuario', max_length=50)
    direccion_mac = models.CharField('Dirección Mac', max_length=50, unique =True, null = True,blank=True)
    direccion_ip = models.CharField('Dirección Ip', max_length=50,unique =True,null = True, blank=True)
    estado = models.BooleanField('Conectado?', default = True)
    observacion = models.TextField('Observación', null=True, blank=True)

    class Meta:
        """Meta definition for AccesoRed."""

        verbose_name = 'Acceso Red'
        verbose_name_plural = 'Acceso Redes'

    def __str__(self):
        """Unicode representation of AccesoRed."""
        return self.usuario

 