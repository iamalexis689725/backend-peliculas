from rest_framework import serializers, viewsets

from peliculas.api import PersonaSerializer, PeliculaSerializer
from peliculas.models import Reparto, Persona, Pelicula


class RepartoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(read_only=True)
    pelicula = PeliculaSerializer(read_only=True)
    persona_id = serializers.PrimaryKeyRelatedField(
        queryset=Persona.objects.all(),
        write_only=True,
        source='persona'
    )
    pelicula_id = serializers.PrimaryKeyRelatedField(
        queryset=Pelicula.objects.all(),
        write_only=True,
        source='pelicula'
    )

    class Meta:
        model = Reparto
        fields = '__all__'

class RepartoViewSet(viewsets.ModelViewSet):
    queryset = Reparto.objects.all()
    serializer_class = RepartoSerializer
    # permission_classes = [IsAuthenticated]
