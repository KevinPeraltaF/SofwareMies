from django.db import models
from ubicacion.models import Distrito
# Modelos del modulo empleado.
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
        self.descripcion = (self.descripcion).upper()
        return super(Area, self).save(*args, **kwargs)


class Cargo(models.Model):
    """Model definition for Cargo."""

    descripcion = models.CharField('Cargo', max_length=50, unique=True)

    class Meta:
        """Meta definition for Cargo."""

        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        """Unicode representation of Cargo."""
        return self.descripcion

    def save(self, *args, **kwargs):
        """Save method for Cargo."""
        self.descripcion = (self.descripcion).upper()
        return super(Cargo, self).save(*args, **kwargs)

    
class UnidadAtencion(models.Model):
    """Model definition for UnidadAtencion."""

    descripcion = models.CharField('Unidad de Atención', max_length=50, unique =True)
    codigo = models.CharField('Código Unidad de atención', max_length=50, unique =True)

    class Meta:
        """Meta definition for UnidadAtencion."""

        verbose_name = 'Unidad de Atención'
        verbose_name_plural = 'Unidad de Atenciones'

    def __str__(self):
        """Unicode representation of UnidadAtencion."""
        return self.descripcion

    def save(self, *args, **kwargs):
        """Save method for UnidadAtencion."""
        self.descripcion = (self.descripcion).upper()
        return super(UnidadAtencion, self).save(*args, **kwargs)


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
        return self.nombres

    def save(self, *args, **kwargs):
        """Save method for Empleado."""
        self.nombres = (self.nombres).upper()
        self.apellidos = (self.apellidos).upper() 
        self.correo =(self.correo).upper()
        return super(Empleado, self).save(*args, **kwargs)


