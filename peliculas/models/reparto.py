from django.db import models


class Reparto(models.Model):
    pelicula = models.ForeignKey(
        'Pelicula',
        on_delete=models.CASCADE,
        related_name='reparto_peliculas'
    )
    persona = models.ForeignKey(
        'Persona',
        on_delete=models.CASCADE,
        related_name='reparto_personas'
    )
    rol = models.BooleanField(default=False)

    def __str__(self):
        rol = "Director" if self.rol else "Persona"
        return f'{self.persona.nombre} - {rol} en {self.pelicula.nombre}'
