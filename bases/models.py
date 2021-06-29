from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) 
    fc = models.DateTimeField(auto_now_add=True) #fecha creacion
    fm = models.DateTimeField(auto_now=True) # fecha modificación
    uc = models.ForeignKey(User, on_delete=models.CASCADE) # usuario creador
    um = models.IntegerField(blank=True, null=True) # usuario modificado
    
    class Meta: #no tomar en cuenta al hacer la migracion
        abstract = True