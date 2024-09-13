from django.contrib import admin

# Register your models here.
from . import models

# admin.site.register(models.Peliculas)
# admin.site.register(models.Director)
# admin.site.register(models.Genero)

from django.contrib import admin
from . import models

@admin.register(models.Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'raiting', 'estreno', 'get_director_name', 'get_generos')
    list_filter = ('generos','raiting')
    date_hierarchy = 'estreno'
    def get_director_name(self, obj):
        return obj.director_origen_id.nombre if obj.director_origen_id else 'Sin Director'
    
    get_director_name.short_description = 'Director'
    
    def get_generos(self, obj):
        return ", ".join(genero.nombre for genero in obj.generos.all())
    
    get_generos.short_description = 'Géneros'

@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'biografia')

@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)