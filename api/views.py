from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .models import (
    Tema, Unidad, Leccion, Usuario, Progreso, PaginaLeccion,
    ContenidoPagina, ImagenPagina, Pregunta, OpcionPregunta, ImagenPregunta
)
from .serializers import (
    UsuarioSerializer, TemaSerializer, UnidadSerializer, LeccionSerializer,
    ProgresoSerializer, PaginaLeccionSerializer, ContenidoPaginaSerializer,
    ImagenPaginaSerializer, PreguntaSerializer, OpcionPreguntaSerializer,
    ImagenPreguntaSerializer, RegistroSerializer
)

# ==========================================
# VISTA DE LOGIN
# ==========================================
class LoginAPIView(APIView):
    permission_classes = [] 
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Por favor, provea username y password."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            
            try:
                perfil = user.perfil 
                perfil_data = UsuarioSerializer(perfil).data
            except Usuario.DoesNotExist:
                perfil_data = None

            return Response({
                "token": token.key,
                "usuario": perfil_data
            }, status=status.HTTP_200_OK)
            
        else:
            return Response(
                {"error": "Credenciales inválidas."},
                status=status.HTTP_401_UNAUTHORIZED
            )

# ==========================================
# VISTA DE REGISTRO
# ==========================================
class RegistroAPIView(APIView):
    permission_classes = [] 
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        if request.FILES:
            data.update(request.FILES)

        serializer = RegistroSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "mensaje": "Usuario y perfil creados exitosamente.", 
                    "usuario_id": user.perfil.id
                },
                status=status.HTTP_201_CREATED
            )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ==========================================
# VISTAS GENERALES (CRUD)
# ==========================================
class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
    permission_classes = []

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
    permission_classes = []

class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer
    permission_classes = []

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = []

class ProgresoViewSet(viewsets.ModelViewSet):
    queryset = Progreso.objects.all()
    serializer_class = ProgresoSerializer
    permission_classes = []

class PaginaLeccionViewSet(viewsets.ModelViewSet):
    queryset = PaginaLeccion.objects.all()
    serializer_class = PaginaLeccionSerializer
    permission_classes = []

class ContenidoPaginaViewSet(viewsets.ModelViewSet):
    queryset = ContenidoPagina.objects.all()
    serializer_class = ContenidoPaginaSerializer
    permission_classes = []

class ImagenPaginaViewSet(viewsets.ModelViewSet):
    queryset = ImagenPagina.objects.all()
    serializer_class = ImagenPaginaSerializer
    permission_classes = []

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = []

class OpcionPreguntaViewSet(viewsets.ModelViewSet):
    queryset = OpcionPregunta.objects.all()
    serializer_class = OpcionPreguntaSerializer
    permission_classes = []

class ImagenPreguntaViewSet(viewsets.ModelViewSet):
    queryset = ImagenPregunta.objects.all()
    serializer_class = ImagenPreguntaSerializer
    permission_classes = []