from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from peliculas.models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    # permission_classes = [IsAuthenticated]