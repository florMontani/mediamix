#forms
from django import forms
from .models import Peliculas
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class PeliculasForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields= "__all__"
        
    def clean_nombre(self):
        nombre: str = self.cleaned_data.get("nombre"," ")
        
    #validar que contenga letras
        if not nombre.isalpha():
            raise ValidationError("el nombre solo debe contener letras")
    #validar la long del nombre de la pelicula       
        if len(nombre)<1 or len(nombre)>20:
            raise ValidationError('el Nombre de la película debe ser mayor a 1 letra pero menor a 20 letras.')
        return nombre
    
    def clean_raiting(self):
        raiting = self.cleaned_data.get("raiting")
        
        # Validar que el raiting esté entre 1 y 10
        if raiting is not None:
            if raiting < 1 or raiting > 10:
                raise ValidationError('El raiting debe estar entre 1 y 10.')
        
        return raiting