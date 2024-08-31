from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Peliculas)
admin.site.register(models.Director)
admin.site.register(models.Genero)