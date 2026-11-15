from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import LoginAPIView, TemaViewSet, UnidadViewSet # ... (importa todos tus ViewSets)
from django.contrib import admin


router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    # Dejamos la ruta base en blanco para que el core le asigne el prefijo
    path('', include(router.urls)),
]