from django.db import models

# Create your models here.

class perfil(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre',max_length = 50, blank = False, null = False)
    apellido = models.CharField('Apellido',max_length = 50, blank = False, null = False)
    telefono = models.CharField('Telefono',max_length = 100, null = False)
    direccion = models.CharField('direccion',max_length = 50, blank = False, null = False)

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['id']

    def __str__(self):
        return self.nombre