from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Tema, Unidad, Leccion, Usuario, Progreso, PaginaLeccion,
    ContenidoPagina, ImagenPagina, Pregunta, OpcionPregunta, ImagenPregunta
)
from .serializers import (
    TemaSerializer, UnidadSerializer, LeccionSerializer, UsuarioSerializer,
    ProgresoSerializer, PaginaLeccionSerializer, ContenidoPaginaSerializer,
    ImagenPaginaSerializer, PreguntaSerializer, OpcionPreguntaSerializer,
    ImagenPreguntaSerializer
)

class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
    permission_classes = [IsAuthenticated]

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
    permission_classes = [IsAuthenticated]

class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer
    permission_classes = [IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class ProgresoViewSet(viewsets.ModelViewSet):
    queryset = Progreso.objects.all()
    serializer_class = ProgresoSerializer
    permission_classes = [IsAuthenticated]

class PaginaLeccionViewSet(viewsets.ModelViewSet):
    queryset = PaginaLeccion.objects.all()
    serializer_class = PaginaLeccionSerializer
    permission_classes = [IsAuthenticated]

class ContenidoPaginaViewSet(viewsets.ModelViewSet):
    queryset = ContenidoPagina.objects.all()
    serializer_class = ContenidoPaginaSerializer
    permission_classes = [IsAuthenticated]

class ImagenPaginaViewSet(viewsets.ModelViewSet):
    queryset = ImagenPagina.objects.all()
    serializer_class = ImagenPaginaSerializer
    permission_classes = [IsAuthenticated]

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [IsAuthenticated]

class OpcionPreguntaViewSet(viewsets.ModelViewSet):
    queryset = OpcionPregunta.objects.all()
    serializer_class = OpcionPreguntaSerializer
    permission_classes = [IsAuthenticated]

class ImagenPreguntaViewSet(viewsets.ModelViewSet):
    queryset = ImagenPregunta.objects.all()
    serializer_class = ImagenPreguntaSerializer
    permission_classes = [IsAuthenticated]
