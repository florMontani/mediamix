from django.db import models
from uuid import uuid4

# def crear_code():
#     return uuid4.hex

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Peliculas(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion =  models.TextField(blank=True,null=True)
    raiting = models.IntegerField(blank=True,null=True)
    estreno = models.DateField(null=True, blank=True)
    # code = models.CharField(max_length=32, default=uuid_md5)
    director_origen_id = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
