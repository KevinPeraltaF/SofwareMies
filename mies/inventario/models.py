from django.db import models
from empleado.models import Empleado, Area
from ubicacion.models import Distrito
import os
from django.db.models.signals import pre_delete, post_delete, pre_save
from django.conf import settings
from django.dispatch import receiver
from django.forms import model_to_dict
# Create your models here.
class Marca(models.Model):
    """Model definition for Marca."""
    descripcion = models.CharField('Marca', max_length=80,unique= True)
  

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

    descripcion = models.CharField('Modelo', max_length=80,unique= True)
  

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

class Procesador(models.Model):
    """Model definition for Procesador."""

    descripcion = models.CharField('Descripción', max_length=80, unique =True)

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

# Create your models here.
class TipoEquipo(models.Model):
    """Model definition for TipoEquipo."""
    descripcion = models.CharField('Tipo Equipo', max_length=80,unique= True)
  

    class Meta:
        """Meta definition for TipoEquipo."""

        verbose_name = 'Tipo Equipo'
        verbose_name_plural = 'Tipo Equipos'

    def __str__(self):
        """Unicode representation of TipoEquipo."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for TipoEquipo."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(TipoEquipo, self).save(*args, **kwargs)

# Create your models here.
class SistemaOperativo(models.Model):
    """Model definition for Equipo."""
    descripcion = models.CharField('Sistema Operativo', max_length=80,unique= True)
  

    class Meta:
        """Meta definition for SistemaOperativo."""

        verbose_name = 'Sistema Operativo'
        verbose_name_plural = 'Sistema Operativos'

    def __str__(self):
        """Unicode representation of SistemaOperativo."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for SistemaOperativo."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(SistemaOperativo, self).save(*args, **kwargs)

# Create your models here.
class SoftwareOfimatica(models.Model):
    """Model definition for SistemaOfimatica."""
    descripcion = models.CharField('Software Ofimática', max_length=80,unique= True)
  

    class Meta:
        """Meta definition for SoftwareOfimatica."""

        verbose_name = 'Software Ofimatica'
        verbose_name_plural = 'Software Ofimatica'

    def __str__(self):
        """Unicode representation of SoftwareOfimatica."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for SoftwareOfimatica."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(SoftwareOfimatica, self).save(*args, **kwargs)

class SoftwareAntivirus(models.Model):
    """Model definition for SoftwareAntivirus."""
    descripcion = models.CharField('Software Antivirus', max_length=80,unique= True)
  

    class Meta:
        """Meta definition for SoftwareAntivirus."""

        verbose_name = 'Software Antivirus'
        verbose_name_plural = 'Software Antivirus'

    def __str__(self):
        """Unicode representation of SoftwareAntivirus."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for SoftwareAntivirus."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(SoftwareAntivirus, self).save(*args, **kwargs)

class ImpresoraTecnologia(models.Model):
    """Model definition for impresoraTecnologia."""
    descripcion = models.CharField('impresora Tecnologia', max_length=80,unique= True)
  

    class Meta:
        """Meta definition for impresoraTecnologia."""

        verbose_name = 'Impresora Tecnologia'
        verbose_name_plural = 'Impresora Tecnologia'

    def __str__(self):
        """Unicode representation of impresoraTecnologia."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for impresoraTecnologia."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(ImpresoraTecnologia, self).save(*args, **kwargs)

class TipoImpresora(models.Model):
    """Model definition for TipoImpresora."""
    descripcion = models.CharField('Tipo Impresora', max_length=80,unique= True)
  

    class Meta:
        """Meta definition for Tipo Impresora."""

        verbose_name = 'Tipo Impresora'
        verbose_name_plural = 'Tipo Impresoras'

    def __str__(self):
        """Unicode representation of TipoImpresora."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for TipoImpresora."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(TipoImpresora, self).save(*args, **kwargs)

class TipoDispositivo(models.Model):
    """Model definition for TipoDispositivo."""
    descripcion = models.CharField('Tipo Dispositivo', max_length=80,unique= True)
  

    class Meta:
        """Meta definition for TipoDispositivo."""

        verbose_name = 'Tipo Dispositivo'
        verbose_name_plural = 'Tipo Dispositivos'

    def __str__(self):
        """Unicode representation of TipoDispositivo."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for TipoDispositivo."""
        self.descripcion = self.descripcion and (self.descripcion).upper()
        return super(TipoDispositivo, self).save(*args, **kwargs)

class Dispositivo(models.Model):
    """Model definition for InventarioTics."""
    lista_categoria= [
    ('1', 'COMPUTADORAS'),
    ('2', 'IMPRESORAS'),
    ('3', 'OTROS DISPOSITIVOS'),]
    categoria = models.CharField('Categoria',max_length=1, choices=lista_categoria, default='1')
    nombreEquipo = models.CharField('Nombre del equipo', max_length=80, null=True,blank=True)
    tipoEquipo = models.ForeignKey(TipoEquipo, on_delete=models.PROTECT, null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True,blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=True,blank=True)
    serie = models.CharField('Serie', max_length=50, unique=True, null=True,blank=True)
    codigoMies = models.CharField('Código Mies', max_length=50, unique=True, null=True,blank=True)
    capacidadProcesador = models.ForeignKey(Procesador,verbose_name="Procesador", on_delete=models.PROTECT, null=True,blank=True)
    capacidadDisco = models.ForeignKey(CapacidadDisco, verbose_name="Capacidad Disco Duro",on_delete=models.PROTECT, null=True,blank=True)
    capacidadMemoriaRam = models.ForeignKey(CapacidadMemoriaRam,verbose_name="Tamaño Memoria Ram", on_delete=models.PROTECT, null=True,blank=True)
    sistemaOperativo = models.ForeignKey(SistemaOperativo, on_delete=models.PROTECT, null=True,blank=True)
    direccionIp = models.CharField('Dirección Ip', max_length=50, unique=True, null=True,blank=True)
    direccionMac = models.CharField('Dirección Mac Address', max_length=50,unique=True, null=True,blank=True)
    ofimatica = models.ForeignKey(SoftwareOfimatica, on_delete=models.PROTECT, null=True,blank=True)
    antivirus = models.ForeignKey(SoftwareAntivirus, on_delete=models.PROTECT, null=True,blank=True)
    softwareAdicional = models.CharField('Software Adicional', max_length=240, null=True, blank=True)

    #impresoras
    tecnologia =models.ForeignKey(ImpresoraTecnologia, on_delete=models.PROTECT, null=True,blank=True)
    tipoImpresora  =models.ForeignKey(TipoImpresora, on_delete=models.PROTECT, null=True,blank=True)
    #otros dispositivos
    tipoDispositivo = models.ForeignKey(TipoDispositivo, on_delete=models.PROTECT, null=True,blank=True)
    lista_estado= [
    ('1', 'BUENO'),
    ('2', 'REGULAR'),
    ('3', 'MALO'),]
    estado = models.CharField('Estado',max_length=1, choices=lista_estado, default='1')
    observacion = models.CharField('Observación', max_length=240 , null=True, blank=True)
    foto = models.ImageField('Foto', upload_to='dispositivo/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for Dispositivo."""

        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'

    def __str__(self):
        if self.codigoMies is None:
           VcodMies= "N/A"
        else:
           VcodMies= self.codigoMies
        if self.serie is None:
           VserMies= "N/A"
        else:
           VserMies= self.serie

        if self.direccionIp is None:
           VdireccionIp= "N/A"
        else:
           VdireccionIp= self.direccionIp

        if self.direccionMac is None:
           VdireccionMac= "N/A"
        else:
           VdireccionMac= self.direccionMac

        if self.nombreEquipo is None:
           VnomEquipo= "N/A"
        else:
           VnomEquipo= self.nombreEquipo
        

        """Unicode representation of Dispositivo."""
        if self.categoria =="1":
            return ("{} - {}- {} - {} - {}").format("COMPUTADORAS",VnomEquipo,VcodMies,VserMies,VdireccionIp,VdireccionMac)
        if self.categoria =="2":
            return ("{} - {} - {} - {} - {}").format("IMPRESORA",VcodMies,VserMies,VdireccionIp,VdireccionMac)
        if self.categoria =="3":
            if self.tipoDispositivo =="1":
                nombreDispositivo ='MONITOR'
            if self.tipoDispositivo =="2":
                nombreDispositivo ='PROYECTOR'
            if self.tipoDispositivo =="3":
                nombreDispositivo ='ESCANER'
            if self.tipoDispositivo =="4":
                nombreDispositivo ='TELEVISOR'
            if self.tipoDispositivo =="5":
                nombreDispositivo ='OTRO'
            return ("{} - {} - {}").format('OTROS DISPOSITIVOS',VcodMies,VserMies)
    
 
    def save(self, *args, **kwargs):
        """Save method for Dispositivo."""
        self.nombreEquipo = self.nombreEquipo and (self.nombreEquipo).upper()
        self.serie = self.serie and  (self.serie).upper() 
        self.codigoMies = self.codigoMies and (self.codigoMies).upper()
        self.softwareAdicional = self.softwareAdicional and (self.softwareAdicional).upper()
        self.observacion = self.observacion and (self.observacion).upper()

        return super(Dispositivo, self).save(*args, **kwargs)
    

@receiver(post_delete, sender=Dispositivo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    ruta = settings.MEDIA_ROOT +"\\"+ str(instance.foto)
    if ruta:
        if os.path.isfile(ruta):
            os.remove(ruta)
@receiver(pre_save, sender=Dispositivo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Dispositivo.objects.get(pk=instance.pk).foto
    except Dispositivo.DoesNotExist:
        return False

    new_file = instance.foto
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)


####################}
###
###
#######################

class InventarioTics(models.Model):
    """Model definition for InventarioTics."""
    cantidad = models.IntegerField('Cantidad', default=1)
    descripcion = models.CharField('Item', max_length=80)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True,blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=True,blank=True)
    serie = models.CharField('Serie', max_length=50, unique=True, null=True,blank=True)
    codigoMies = models.CharField('Código Mies', max_length=50, unique=True, null=True,blank=True)
    lista_condicion = [
    ('1', 'NUEVO'),
    ('2', 'REGULAR'),
    ('3', 'DAÑADO'),]
    condicion = models.CharField('Condición',max_length=1, choices=lista_condicion, null=True, blank=True)
    foto = models.ImageField('Foto', upload_to='InventarioTics/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for InventarioTics."""

        verbose_name = 'Inventario Tics'
        verbose_name_plural = 'Inventario Tics'

    def __str__(self):
        if self.codigoMies is None:
           VcodMies= "N/A"
        else:
           VcodMies= self.codigoMies
        if self.serie is None:
           VserMies= "N/A"
        else:
           VserMies= self.serie
        

        """Unicode representation of InventarioTics."""
        return ("{} - {}- {} - {}- {}").format(self.descripcion,self.marca, self.modelo,VcodMies,VserMies)
    
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
