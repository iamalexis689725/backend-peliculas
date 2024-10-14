from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='static/personas/', null=True, blank=True)

    def __str__(self):
        return self.nombre
