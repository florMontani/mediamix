from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.nombre
    
class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre
        
class Peliculas(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion =  models.TextField(blank=True,null=True)
    raiting = models.IntegerField(blank=True,null=True,validators=[
            MinValueValidator(1), 
            MaxValueValidator(10)
        ])
    estreno = models.DateField(null=True, blank=True)
    director_origen_id = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)
    generos = models.ManyToManyField(Genero, related_name='peliculas')
    def __str__(self):
        return self.nombre
    