from django.db import models

# Create your models here.
class Zona(models.Model):
    """Model definition for Zona."""

    descripcion = models.CharField('Zona', max_length=50, unique=True)

    class Meta:
        """Meta definition for Zona."""

        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        """Save method for Zona."""
        self.descripcion = (self.descripcion).upper()
        return super(Zona, self).save(*args, **kwargs)


class Provincia(models.Model):
    """Model definition for Provincia."""
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    descripcion = models.CharField('Provincia', max_length=50, unique=True)

    class Meta:
        """Meta definition for Provincia."""

        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.descripcion
    
    def save(self, *args, **kwargs):
        """Save method for Provincia."""
        self.descripcion = (self.descripcion).upper()
        return super(Provincia, self).save(*args, **kwargs)


class Distrito(models.Model):
    """Model definition for Distrito."""
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    descripcion = models.CharField('Distrito', max_length=50, unique=True)

    class Meta:
        """Meta definition for Distrito."""

        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'

    def __str__(self):
        """Unicode representation of Distrito."""
        return self.descripcion

    
    def save(self, *args, **kwargs):
        """Save method for Distrito."""
        self.descripcion = (self.descripcion).upper()
        return super(Distrito, self).save(*args, **kwargs)

