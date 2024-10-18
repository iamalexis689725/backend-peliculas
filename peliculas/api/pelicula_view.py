from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from peliculas.models import Pelicula


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    # permission_classes = [IsAuthenticated]