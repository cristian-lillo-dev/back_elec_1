from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import LoginAPIView, TemaViewSet, UnidadViewSet # ... (importa todos tus ViewSets)

router = DefaultRouter()
router.register(r'temas', TemaViewSet, basename='tema')
router.register(r'unidades', UnidadViewSet, basename='unidad')
# ... (registra el resto de los ViewSets)

urlpatterns = [
    path('auth/login/', LoginAPIView.as_view(), name='api-login'),
    # Dejamos la ruta base en blanco para que el core le asigne el prefijo
    path('', include(router.urls)),
]