from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    biografia =  models.TextField(blank=True,null=True, verbose_name = 'biografía')

    def __str__(self):
        return self.nombre
    @property
    def peliculas(self):
        return self.peliculas_director.all()
    
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'
    
class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre
        
class Peliculas(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion =  models.TextField(blank=True,null=True,  verbose_name = 'descripción')
    raiting = models.FloatField(blank=True,null=True,validators=[
            MinValueValidator(1.0), 
            MaxValueValidator(10.0)
        ])
    estreno = models.DateField(null=True, blank=True)
    director_origen_id = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True, related_name='peliculas_director', verbose_name="Director")
    generos = models.ManyToManyField(Genero, related_name='peliculas')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
    