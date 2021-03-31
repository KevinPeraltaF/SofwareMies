from django.db import models
from empleado.models import Empleado, Area
from ubicacion.models import Distrito
# Create your models here.
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
        self.descripcion = (self.descripcion).upper()
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
        self.descripcion = (self.descripcion).upper()
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
        self.descripcion = (self.descripcion).upper()
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
        self.descripcion = (self.descripcion).upper()
        return super(Condicion, self).save(*args, **kwargs)


class InventarioTics(models.Model):
    """Model definition for InventarioTics."""

    fechaIngreso = models.DateField('Fecha Ingreso', auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripción / Nombre', max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    condicion = models.ForeignKey(Condicion, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=50, unique=True, null=True,blank=True)
    codigoMies = models.CharField('Código Mies', max_length=50, unique=True, null=True,blank=True)
    cantidad = models.IntegerField('Cantidad', default=0)
    foto = models.ImageField('Foto', upload_to='InventarioTics/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for InventarioTics."""

        verbose_name = 'Inventario Tics'
        verbose_name_plural = 'Inventario Tics'

    def __str__(self):
        """Unicode representation of InventarioTics."""
        return self.descripcion

    def save(self, *args, **kwargs):
        """Save method for InventarioTics."""
        self.descripcion =(self.descripcion).upper()
        self.serie =(self.serie).upper()
        self.codigoMies =(self.codigoMies).upper()
        return super(InventarioTics, self).save(*args, **kwargs)





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
        self.descripcion = (self.descripcion).upper()
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
        self.descripcion = (self.descripcion).upper()
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
        self.descripcion = (self.descripcion).upper()
        return super(Procesador, self).save(*args, **kwargs)


class InvetarioDistritoCabecera(models.Model):
    """Model definition for InvetarioDistritoCabecera."""

    fechaIngreso = models.DateField('Fecha Ingreso', auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Area, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripción / Nombre', max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    condicion = models.ForeignKey(Condicion, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=50, default='N/A', unique=True, null=True,blank=True)
    codigoMies = models.CharField('Código Mies', max_length=50, default='N/A',unique=True, null=True,blank=True)
    direccionIp = models.CharField('Dirección Ip', max_length=50, default='N/A',unique=True, null=True,blank=True)
    direccionMac = models.CharField('Dirección Mac Address', default='N/A', max_length=50,unique=True, null=True,blank=True)
    capacidadDisco = models.ForeignKey(CapacidadDisco, on_delete=models.CASCADE, null=True,blank=True)
    capacidadMemoria = models.ForeignKey(CapacidadMemoriaRam, on_delete=models.CASCADE, null=True,blank=True)
    capacidadProcesador = models.ForeignKey(Procesador, on_delete=models.CASCADE, null=True,blank=True)
    foto = models.ImageField('Foto', upload_to='InventarioDistrito/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        """Meta definition for InvetarioDistritoCabecera."""

        verbose_name = 'Invetario Distrito '
        verbose_name_plural = 'Invetario Distrito '

    def __str__(self):
        """Unicode representation of InvetarioDistritoCabecera."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for InvetarioDistritoCabecera."""
        self.descripcion =(self.descripcion).upper()
        self.serie =(self.serie).upper()
        self.codigoMies =(self.codigoMies).upper()
        return super(InvetarioDistritoCabecera, self).save(*args, **kwargs)



class InventarioDistritoDetalle(models.Model):
    """Model definition for InventarioDistritoDetalle."""

    cabeceraDistrito = models.ForeignKey(InvetarioDistritoCabecera, on_delete=models.CASCADE)
    periferico = models.ForeignKey(InventarioTics, on_delete=models.CASCADE, null=True,blank=True)
    cantidad = models.IntegerField('Cantidad', default=1)
    class Meta:
        """Meta definition for InventarioDistritoDetalle."""

        verbose_name = 'Inventario Distrito Detalle'
        verbose_name_plural = 'Inventario Distrito Detalles'

    def __int__(self):
        return self.periferico
        """Unicode representation of InventarioDistritoDetalle."""
        return self.periferico



# Create your models here.
