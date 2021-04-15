from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField( 
    upload_to='user/pictures',
     height_field=None, 
     width_field=None, 
     max_length=None)