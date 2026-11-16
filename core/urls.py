from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Conecta las rutas de tu aplicación 'api'. 
    # Todo lo que envíes a midominio.com/api/ irá al archivo api/urls.py
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)