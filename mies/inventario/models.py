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


class Dispositivo(models.Model):
    """Model definition for InventarioTics."""
    lista_categoria= [
    ('1', 'COMPUTADORAS'),
    ('2', 'IMPRESORAS'),
    ('3', 'OTROS DISPOSITIVOS'),]
    categoria = models.CharField('Categoria',max_length=1, choices=lista_categoria, default='1')
    nombreEquipo = models.CharField('Nombre del equipo', max_length=80, null=True,blank=True)
    lista_tipoEquipo= [
    ('1', 'ALL IN ONE'),
    ('2', 'DESKTOP'),
    ('3', 'LAPTOP'),
    ('4', 'SERVIDOR'),]
    tipoEquipo = models.CharField('Tipo Equipo',max_length=1, choices=lista_tipoEquipo , null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True,blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=True,blank=True)
    serie = models.CharField('Serie', max_length=50, unique=True, null=True,blank=True)
    codigoMies = models.CharField('Código Mies', max_length=50, unique=True, null=True,blank=True)
    capacidadProcesador = models.ForeignKey(Procesador,verbose_name="Procesador", on_delete=models.PROTECT, null=True,blank=True)
    capacidadDisco = models.ForeignKey(CapacidadDisco, verbose_name="Capacidad Disco Duro",on_delete=models.PROTECT, null=True,blank=True)
    capacidadMemoriaRam = models.ForeignKey(CapacidadMemoriaRam,verbose_name="Tamaño Memoria Ram", on_delete=models.PROTECT, null=True,blank=True)
    lista_sistemaOperativos = [
    ('1', 'WINDOWS XP'),
    ('2', 'WINDOWS VISTA'),
    ('3', 'WINDOWS 7'),
    ('4', 'WINDOWS 8'),
    ('5', 'WINDOWS 10'),
    ('6', 'LINUX'),
    ('7', 'IOS'),
    ('8', 'OTROS'),]
    sistemaOperativo = models.CharField('Sistema Operativo',max_length=1, choices=lista_sistemaOperativos, null=True, blank=True)
    direccionIp = models.CharField('Dirección Ip', max_length=50, unique=True, null=True,blank=True)
    direccionMac = models.CharField('Dirección Mac Address', max_length=50,unique=True, null=True,blank=True)
    

    lista_ofimatica= [
    ('1', 'MICROSOFT OFFICE'),
    ('2', 'LIBRE OFFICE'),
    ('3', 'OPEN OFFICE'),
    ('4', 'OTROS'),]
    ofimatica = models.CharField('Software Ofimática',max_length=1, choices=lista_ofimatica , null=True, blank=True)

    lista_antivirus= [
    ('1', 'KASPERSKY'),
    ('2', 'AVAST'),
    ('3', 'AVG'),
    ('4', 'ESET'),
    ('5', 'AVIRA'),
    ('6', 'OTRO'),]
    antivirus = models.CharField('Software Antivirus',max_length=1, choices=lista_antivirus , null=True, blank=True)

    softwareAdicional = models.CharField('Software Adicional', max_length=240, null=True, blank=True)


    #impresoras
    lista_tecnologia= [
    ('1', 'LASER'),
    ('2', 'MATRICIAL'),
    ('3', 'INYECCIÓN A TINTA'),
    ]
    tecnologia = models.CharField('Tecnologia',max_length=1, choices=lista_tecnologia, null=True, blank=True)
    lista_tipoImpresora= [
    ('1', 'MULTIFUNCIÓN B/N'),
    ('2', 'MULTIFUNCIÓN COLOR'),
    ('3', 'SIMPLE B/N'),
    ('4', 'SIMPLE COLOR'),]
    tipoImpresora = models.CharField('Tipo Impresora',max_length=1, choices=lista_tipoImpresora, null=True, blank=True)
    #otros dispositivos
    lista_tipoDispositivo= [
    ('1', 'MONITOR'),
    ('2', 'PROYECTOR'),
    ('3', 'ESCANER'),
    ('4', 'TELEVISOR'),
    ('5', 'OTRO'),
    ]
    tipoDispositivo = models.CharField('Tipo Dispositivo',max_length=1, choices=lista_tipoDispositivo, null=True, blank=True)


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
        

        """Unicode representation of Dispositivo."""
        if self.categoria =="1":
            return ("{} - {}- {} - {} - {}").format(self.nombreEquipo,VcodMies,VserMies,VdireccionIp,VdireccionMac)
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