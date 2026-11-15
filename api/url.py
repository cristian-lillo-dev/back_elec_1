from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LoginAPIView, RegistroAPIView, TemaViewSet, UnidadViewSet, LeccionViewSet, 
    UsuarioViewSet, ProgresoViewSet, PaginaLeccionViewSet, 
    ContenidoPaginaViewSet, ImagenPaginaViewSet, PreguntaViewSet, 
    OpcionPreguntaViewSet, ImagenPreguntaViewSet
)

router = DefaultRouter()
router.register(r'temas', TemaViewSet, basename='tema')
router.register(r'unidades', UnidadViewSet, basename='unidad')
router.register(r'lecciones', LeccionViewSet, basename='leccion')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'progresos', ProgresoViewSet, basename='progreso')
router.register(r'paginas', PaginaLeccionViewSet, basename='pagina')
router.register(r'contenidos-pagina', ContenidoPaginaViewSet, basename='contenido-pagina')
router.register(r'imagenes-pagina', ImagenPaginaViewSet, basename='imagen-pagina')
router.register(r'preguntas', PreguntaViewSet, basename='pregunta')
router.register(r'opciones-pregunta', OpcionPreguntaViewSet, basename='opcion-pregunta')
router.register(r'imagenes-pregunta', ImagenPreguntaViewSet, basename='imagen-pregunta')

urlpatterns = [
    # Rutas de Autenticación
    path('auth/login/', LoginAPIView.as_view(), name='api-login'),
    path('auth/registro/', RegistroAPIView.as_view(), name='api-registro'),
    
    # Inclusión automática de las rutas de los modelos
    path('', include(router.urls)),
]