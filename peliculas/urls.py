from rest_framework.routers import DefaultRouter
from peliculas.api import PersonaViewSet, PeliculaViewSet

router = DefaultRouter()

router.register(r'personas', PersonaViewSet, basename='persona')
router.register(r'peliculas', PeliculaViewSet, basename='pelicula')

urlpatterns = router.urls