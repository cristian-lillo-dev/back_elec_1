from django.contrib import admin
from .models import (
    Tema, Unidad, Leccion, Usuario, Progreso, PaginaLeccion,
    ContenidoPagina, ImagenPagina, Pregunta, OpcionPregunta, ImagenPregunta
)

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero_tema')
    search_fields = ('nombre', 'descripcion')
    ordering = ('numero_tema',)

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero_unidad', 'tema')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('tema',)
    ordering = ('tema', 'numero_unidad')

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero_leccion', 'unidad')
    search_fields = ('nombre',)
    list_filter = ('unidad__tema', 'unidad')
    ordering = ('unidad', 'numero_leccion')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'imagen')
    search_fields = ('user__username', 'user__email')

@admin.register(Progreso)
class ProgresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'leccion')
    list_filter = ('usuario', 'leccion')
    search_fields = ('usuario__user__username', 'leccion__nombre')

@admin.register(PaginaLeccion)
class PaginaLeccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_pagina', 'leccion')
    list_filter = ('leccion',)
    ordering = ('leccion', 'numero_pagina')

@admin.register(ContenidoPagina)
class ContenidoPaginaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_contenido_pagina', 'pagina_leccion')
    search_fields = ('texto',)
    list_filter = ('pagina_leccion',)

@admin.register(ImagenPagina)
class ImagenPaginaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_imagen_pagina', 'pagina_leccion')
    list_filter = ('pagina_leccion',)

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_pregunta', 'texto', 'pagina_leccion')
    search_fields = ('texto',)
    list_filter = ('pagina_leccion',)

@admin.register(OpcionPregunta)
class OpcionPreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'es_correcta', 'pregunta')
    list_filter = ('es_correcta', 'pregunta')
    search_fields = ('texto', 'pregunta__texto')

@admin.register(ImagenPregunta)
class ImagenPreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero_imagen_pregunta', 'pregunta')
    search_fields = ('nombre',)