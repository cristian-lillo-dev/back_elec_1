from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Conecta las rutas de tu aplicación (el prefijo 'api/' se aplicará a todas)
    # Nota: Si la carpeta de tu app no se llama 'api', cambia 'api.urls' por 'tu_app.urls'
    path('api/', include('api.urls')),
]