from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Tema, Unidad, Leccion, Usuario, Progreso, PaginaLeccion,
    ContenidoPagina, ImagenPagina, Pregunta, OpcionPregunta, ImagenPregunta
)

class UserDjangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UsuarioSerializer(serializers.ModelSerializer):
    user = UserDjangoSerializer(read_only=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'user', 'imagen']

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'

class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = '__all__'

class ProgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progreso
        fields = '__all__'

class ContenidoPaginaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenidoPagina
        fields = '__all__'

class ImagenPaginaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenPagina
        fields = '__all__'

class PaginaLeccionSerializer(serializers.ModelSerializer):
    contenidos = ContenidoPaginaSerializer(many=True, read_only=True)
    imagenes = ImagenPaginaSerializer(many=True, read_only=True)

    class Meta:
        model = PaginaLeccion
        fields = ['id', 'numero_pagina', 'leccion', 'contenidos', 'imagenes']

class OpcionPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionPregunta
        fields = ['id', 'texto', 'es_correcta']

class ImagenPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenPregunta
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionPreguntaSerializer(many=True, read_only=True)
    imagenes = ImagenPreguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ['id', 'texto', 'pagina_leccion', 'numero_pregunta', 'opciones', 'imagenes']