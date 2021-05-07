from django.db import models
from ubicacion.models import Distrito
import os
from django.db.models.signals import pre_delete, post_delete, pre_save
from django.conf import settings
from django.dispatch import receiver
# Modelos del modulo empleado.
#modelo AREA
class Area(models.Model):
    """Model definition for area."""
    distrito = models.ForeignKey(Distrito, on_delete=models.PROTECT)
    descripcion = models.CharField('Area', max_length=50, unique=True)

    class Meta:
        """Meta definition for area."""

        verbose_name = 'area'
        verbose_name_plural = 'areas'

    def __str__(self):
        """Unicode representation of area."""
        return self.descripcion

    def save(self, *args, **kwargs):
        """Save method for Area."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Area, self).save(*args, **kwargs)

#modelo CARGO
class Cargo(models.Model):
    """Model definition for Cargo."""

    descripcion = models.CharField('Cargo', max_length=100, unique=True)

    class Meta:
        """Meta definition for Cargo."""

        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        """Unicode representation of Cargo."""
        return self.descripcion

    def save(self, *args, **kwargs):
        """Save method for Cargo."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Cargo, self).save(*args, **kwargs)

 #modelo UNIDAD DE ATENCION   
class UnidadAtencion(models.Model):
    """Model definition for UnidadAtencion."""

    descripcion = models.CharField('Unidad de Atención', max_length=50, unique =True)
    codigo = models.CharField('Código Unidad de Atención', max_length=50, unique =True)

    class Meta:
        """Meta definition for UnidadAtencion."""

        verbose_name = 'Unidad de Atención'
        verbose_name_plural = 'Unidad de Atenciones'

    def __str__(self):
        """Unicode representation of UnidadAtencion."""
        return self.descripcion

    def save(self, *args, **kwargs):
        """Save method for UnidadAtencion."""
        self.descripcion =self.descripcion and (self.descripcion).upper()
        return super(UnidadAtencion, self).save(*args, **kwargs)

#modelo EMPLEADO
class Empleado(models.Model):
    """Model definition for Empleado."""

    fecha = models.DateField('Fecha Ingreso', auto_now=False, auto_now_add=False)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    unidadAtencion = models.ForeignKey(UnidadAtencion,verbose_name='Unidad de Atención',on_delete=models.PROTECT, null=True , blank= True)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    lista_genero = [
    ('1', 'MASCULINO'),
    ('2', 'FEMENINO'),
    ('3', 'GLBTI'),]
    genero = models.CharField('Género',max_length=1, choices=lista_genero, default='2')
    correo = models.EmailField('Correo', max_length=254, unique= True)
    cedula = models.CharField('Cédula', max_length=10, null=True, blank=True, unique = True)
    telefono = models.CharField('Télefono móvil', max_length=10, null=True, blank=True)
    foto = models.ImageField('Foto', upload_to='Empleados/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    estado = models.BooleanField('Estado', default = True)
    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return ("{} {}").format(self.apellidos, self.nombres)

    def save(self, *args, **kwargs):
        """Save method for Empleado."""
        self.nombres = self.nombres and (self.nombres).upper()
        self.apellidos = self.apellidos and (self.apellidos).upper() 
        self.correo =self.correo and (self.correo).upper()
        return super(Empleado, self).save(*args, **kwargs)

@receiver(post_delete, sender=Empleado)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    ruta = settings.MEDIA_ROOT +"\\"+ str(instance.foto)
    print(ruta)
    if ruta:
        if os.path.isfile(ruta):
            os.remove(ruta)
@receiver(pre_save, sender=Empleado)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Empleado.objects.get(pk=instance.pk).foto
    except Empleado.DoesNotExist:
        return False

    new_file = instance.foto
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)
