from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

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
    imagen = models.ImageField(upload_to='imagenes_peliculas/', blank=True, null=True, verbose_name='Imagen')
   
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

class Premium(models.Model):
    plan = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self) -> str:
        return f'{self.plan} - ${self.precio}'

    class Meta:
        verbose_name = 'Plan Premium'
        verbose_name_plural = 'Planes Premium'

    def save(self, *args, **kwargs):
        if self.precio < 0:
            raise ValidationError('El precio no puede ser negativo.')
        super().save(*args, **kwargs)
