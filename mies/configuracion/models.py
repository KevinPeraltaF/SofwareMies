from django.db import models
from empleado.models import Empleado
import os
from django.db.models.signals import pre_delete, post_delete, pre_save
from django.conf import settings
from django.dispatch import receiver
# Create your models here.
class Configuracion(models.Model):
    """Model definition for Configuracion."""

    encargadoTics = models.ForeignKey(Empleado,verbose_name='Encargado Tics', on_delete=models.PROTECT)
    encargadoBienes = models.ForeignKey(Empleado,related_name="encargadoBienes",verbose_name='Encargado Bienes', on_delete=models.PROTECT)
    logoIzquierdo = models.ImageField('Logo izquierdo', upload_to='Logos/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    logocentro = models.ImageField('Logo centro', upload_to='Logos/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    logoDerecho = models.ImageField('Logo derecho', upload_to='Logos/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for Configuracion."""

        verbose_name = 'Configuracion'
        verbose_name_plural = 'Configuraciones'

    def __str__(self):
        """Unicode representation of Configuracion."""
        return str(self.encargadoTics)


@receiver(post_delete, sender=Configuracion)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    ruta = settings.MEDIA_ROOT +"\\"+ str(instance.logoIzquierdo)
    if ruta:
        if os.path.isfile(ruta):
            os.remove(ruta)
@receiver(pre_save, sender=Configuracion)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Configuracion.objects.get(pk=instance.pk).logoIzquierdo
    except Configuracion.DoesNotExist:
        return False

    new_file = instance.logoIzquierdo
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)


########
receiver(post_delete, sender=Configuracion)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    ruta = settings.MEDIA_ROOT +"\\"+ str(instance.logocentro)
    if ruta:
        if os.path.isfile(ruta):
            os.remove(ruta)
@receiver(pre_save, sender=Configuracion)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Configuracion.objects.get(pk=instance.pk).logocentro
    except Configuracion.DoesNotExist:
        return False

    new_file = instance.logocentro
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)



########
receiver(post_delete, sender=Configuracion)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    ruta = settings.MEDIA_ROOT +"\\"+ str(instance.logoDerecho)
    if ruta:
        if os.path.isfile(ruta):
            os.remove(ruta)
@receiver(pre_save, sender=Configuracion)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Configuracion.objects.get(pk=instance.pk).logoDerecho
    except Configuracion.DoesNotExist:
        return False

    new_file = instance.logoDerecho
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)
