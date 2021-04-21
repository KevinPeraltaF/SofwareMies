from django.db import models
from empleado.models import Empleado, Area
from ubicacion.models import Distrito
import os
from django.db.models.signals import pre_delete, post_delete, pre_save
from django.conf import settings
from django.dispatch import receiver

from django.forms import model_to_dict
# Create your models here
class Marca(models.Model):
    """Model definition for Marca."""
    descripcion = models.CharField('Marca', max_length=50,unique= True)
  

    class Meta:
        """Meta definition for Marca."""

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        """Unicode representation of Marca."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Marca."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Marca, self).save(*args, **kwargs)

class Modelo(models.Model):
    """Model definition for Modelo."""

    descripcion = models.CharField('Modelo', max_length=50,unique= True)
  

    class Meta:
        """Meta definition for Modelo."""

        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        """Unicode representation of Modelo."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Modelo."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Modelo, self).save(*args, **kwargs)



class Categoria(models.Model):
    """Model definition for Categoria."""

    descripcion = models.CharField('Categoria', max_length=50,unique= True)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Categoria."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Categoria, self).save(*args, **kwargs)


class Condicion(models.Model):
    """Model definition for Condicion."""

    descripcion = models.CharField('Condicion', max_length=50,unique= True)

    class Meta:
        """Meta definition for Condicion."""

        verbose_name = 'Condicion'
        verbose_name_plural = 'Condiciones'

    def __str__(self):
        """Unicode representation of Condicion."""
        return self.descripcion 

    def save(self,*args, **kwargs):
        """Save method for Condicion."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Condicion, self).save(*args, **kwargs)


class InventarioTics(models.Model):
    """Model definition for InventarioTics."""

    fechaIngreso = models.DateField('Fecha Ingreso', auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    ubicacion = models.ForeignKey(Area, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descripcion = models.CharField('Descripción / Nombre', max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True,blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=True,blank=True)
    condicion = models.ForeignKey(Condicion, on_delete=models.PROTECT)
    serie = models.CharField('Serie', max_length=50, unique=True, null=True,blank=True)
    codigoMies = models.CharField('Código Mies', max_length=50, unique=True, null=True,blank=True)
    cantidad = models.IntegerField('Cantidad', default=1)
    foto = models.ImageField('Foto', upload_to='InventarioTics/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for InventarioTics."""

        verbose_name = 'Inventario Tics'
        verbose_name_plural = 'Inventario Tics'

    def __str__(self):
        """Unicode representation of InventarioTics."""
        return self.descripcion
    
    def toJSON(self):
        item = model_to_dict(self)
        item['cantidad'] = self.cantidad
        return item
    def save(self, *args, **kwargs):
        """Save method for InventarioTics."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        self.serie = self.serie and  (self.serie).upper()
        self.codigoMies = self.codigoMies and (self.codigoMies).upper()
        return super(InventarioTics, self).save(*args, **kwargs)
    

@receiver(post_delete, sender=InventarioTics)
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
@receiver(pre_save, sender=InventarioTics)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = InventarioTics.objects.get(pk=instance.pk).foto
    except InventarioTics.DoesNotExist:
        return False

    new_file = instance.foto
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)


class CapacidadDisco(models.Model):
    """Model definition for CapacidadDisco."""

    descripcion = models.CharField('Descripción', max_length=50, unique =True)

    class Meta:
        """Meta definition for CapacidadDisco."""

        verbose_name = 'Capacidad Disco'
        verbose_name_plural = 'Capacidad Discos'

    def __str__(self):
        """Unicode representation of CapacidadDisco."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for CapacidadDisco."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(CapacidadDisco, self).save(*args, **kwargs)


class CapacidadMemoriaRam(models.Model):
    """Model definition for CapacidadMemoriaRam."""

    descripcion = models.CharField('Descripción', max_length=50, unique =True)

    class Meta:
        """Meta definition for CapacidadMemoriaRam."""

        verbose_name = 'Capacidad Memoria Ram'
        verbose_name_plural = 'Capacidad Memoria Ram'

    def __str__(self):
        """Unicode representation of CapacidadMemoriaRam."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for CapacidadMemoriaRam."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(CapacidadMemoriaRam, self).save(*args, **kwargs)

    # TODO: Define custom methods here


   
class Procesador(models.Model):
    """Model definition for Procesador."""

    descripcion = models.CharField('Descripción', max_length=50, unique =True)

    class Meta:
        """Meta definition for Procesador."""

        verbose_name = 'Procesador'
        verbose_name_plural = 'Procesadores'
    def __str__(self):
        """Unicode representation of Procesador."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Procesador."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(Procesador, self).save(*args, **kwargs)


class InvetarioDistritoCabecera(models.Model):
    """Model definition for InvetarioDistritoCabecera."""

    fechaIngreso = models.DateField('Fecha Ingreso', auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    ubicacion = models.ForeignKey(Area, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descripcion = models.CharField('Descripción / Nombre', max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    condicion = models.ForeignKey(Condicion, on_delete=models.PROTECT)
    serie = models.CharField('Serie', max_length=50,  unique=True, null=True,blank=True)
    codigoMies = models.CharField('Código Mies', max_length=50, unique=True, null=True,blank=True)
    direccionIp = models.CharField('Dirección Ip', max_length=50, unique=True, null=True,blank=True)
    direccionMac = models.CharField('Dirección Mac Address', max_length=50,unique=True, null=True,blank=True)
    capacidadDisco = models.ForeignKey(CapacidadDisco, on_delete=models.PROTECT, null=True,blank=True)
    capacidadMemoria = models.ForeignKey(CapacidadMemoriaRam, on_delete=models.PROTECT, null=True,blank=True)
    capacidadProcesador = models.ForeignKey(Procesador, on_delete=models.PROTECT, null=True,blank=True)
    foto = models.ImageField('Foto', upload_to='InventarioDistrito/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for InvetarioDistritoCabecera."""

        verbose_name = 'Invetario Distrito '
        verbose_name_plural = 'Invetario Distrito '

    def toJSON(self):
        item = model_to_dict(self)
        item['det']= [i.toJSON() for i in self.inventariodistritodetalle_set.all()]
        return item
    def __str__(self):
        """Unicode representation of InvetarioDistritoCabecera."""
        return ("{}- {}- {}- {}").format(self.descripcion, self.responsable, self.serie, self.codigoMies)

    def save(self,*args, **kwargs):
        """Save method for InvetarioDistritoCabecera."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        self.serie =self.serie and (self.serie).upper()
        self.codigoMies = self.codigoMies and (self.codigoMies).upper()
        return super(InvetarioDistritoCabecera, self).save(*args, **kwargs)



class InventarioDistritoDetalle(models.Model):
    """Model definition for InventarioDistritoDetalle."""

    cabeceraDistrito = models.ForeignKey(InvetarioDistritoCabecera,related_name='items', on_delete=models.CASCADE)
    periferico = models.ForeignKey(InventarioTics, on_delete=models.PROTECT, null=True,blank=True)
    cantidad = models.IntegerField('Cantidad', default=1)
    class Meta:
        """Meta definition for InventarioDistritoDetalle."""

        verbose_name = 'Inventario Distrito Detalle'
        verbose_name_plural = 'Inventario Distrito Detalles'
    def toJSON(self):
        item = model_to_dict(self, exclude=['cabeceraDistrito'])
        item['periferico'] = self.periferico.toJSON()
        item['cantidad'] = self.cantidad
        return item

    def __int__(self):
        """Unicode representation of InventarioDistritoDetalle."""
        return self.periferico



# Create your models here.
