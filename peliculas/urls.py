from rest_framework.routers import DefaultRouter
from peliculas.api import PersonaViewSet, PeliculaViewSet, UserViewSet
from peliculas.api.reparto_view import RepartoViewSet

router = DefaultRouter()

router.register(r'personas', PersonaViewSet, basename='persona')
router.register(r'peliculas', PeliculaViewSet, basename='pelicula')
router.register(r'reparto', RepartoViewSet, basename='reparto')
router.register(r'auth', UserViewSet, basename='auth')
urlpatterns = router.urls