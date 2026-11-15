from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Conecta las rutas de tu aplicación 'api'. 
    # Todo lo que envíes a midominio.com/api/ irá al archivo api/urls.py
    path('api/', include('api.urls')),
]