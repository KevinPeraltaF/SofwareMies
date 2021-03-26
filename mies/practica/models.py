from django.db import models
from empleado.models import Empleado
# Create your models here.
class Universidad(models.Model):
    """Model definition for Universidad."""

    descripcion = models.CharField('Universidad', max_length=50,unique = True)

    class Meta:
        """Meta definition for Universidad."""

        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'

    def __str__(self):
        """Unicode representation of Universidad."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Universidad."""
        self.descripcion =(self.descripcion).upper()
        return super(Universidad, self).save(*args, **kwargs)


class Carrera(models.Model):
    """Model definition for Carrera."""

    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    descripcion = models.CharField('Carrera', max_length=50,unique = True)

    class Meta:
        """Meta definition for Carrera."""

        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def __str__(self):
        """Unicode representation of Carrera."""
        return self.descripcion

    def save(self,*args, **kwargs):
        """Save method for Carrera."""
        self.descripcion =(self.descripcion).upper()
        return super(Carrera, self).save(*args, **kwargs)


class Pasante(models.Model):
    """Model definition for Pasante."""

    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    fecha_inicio = models.DateField('Fecha Incio', auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField('Fecha Fin', auto_now=False, auto_now_add=False, null= True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    horas_diarias = models.IntegerField('Horas Diarias', default =0)
    cedula = models.CharField('Cédula', max_length=10)
    telefono = models.CharField('Télefono Movil', max_length=10)
    tutor_profesional = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    estado = models.BooleanField('Prácticas profesionales completadas?')
    class Meta:
        """Meta definition for Pasante."""

        verbose_name = 'Pasante'
        verbose_name_plural = 'Pasantes'

    def __str__(self):
        """Unicode representation of Pasante."""
        return self.apellidos

    def save(self,*args, **kwargs):
        """Save method for Pasante."""
        self.nombres =(self.nombres).upper()
        self.apellidos =(self.apellidos).upper()
        return super(Pasante, self).save(*args, **kwargs)



# Create your models here.
