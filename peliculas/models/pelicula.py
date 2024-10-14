from django.db import models


class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    imagen = models.ImageField(upload_to='static/peliculas/', null=True, blank=True)
    fecha_lanzamiento = models.DateField()
    calificacion = models.IntegerField()
    trailer = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre