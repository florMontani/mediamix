from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Usuariopremium(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario_premium")
    celular = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return f'{self.usuario.username} ({self.celular})'

    class Meta:
        verbose_name = 'Usuario Premium'
        verbose_name_plural = 'Usuarios Premium'
        

class AccesoPremium(models.Model):
    usuario_premium = models.ForeignKey(Usuariopremium, on_delete=models.DO_NOTHING, related_name='accesos_premium')
    plan = models.ForeignKey('peliculas.Premium', on_delete=models.DO_NOTHING)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_inicio = models.DateTimeField(default=timezone.now, editable=False)
    fecha_fin = models.DateTimeField(editable=False)
    
    class Meta:
        verbose_name = 'Acceso Premium'
        verbose_name_plural = 'Accesos Premium'

    @property
    def duracion_alquiler(self):
        return self.fecha_fin - self.fecha_inicio

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo calcular cuando se crea una nueva instancia
            if self.plan:
                self.precio_total = self.plan.precio
                self.fecha_fin = self.fecha_inicio + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.usuario_premium} - ${self.precio_total}'

    class Meta:
        ordering = ['-fecha_inicio']
