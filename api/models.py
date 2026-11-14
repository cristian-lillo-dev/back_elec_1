from django.db import models
from django.contrib.auth.models import User

class Tema(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='temas/', null=True, blank=True)
    numero_tema = models.IntegerField()

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    pdf_url = models.URLField(max_length=500, blank=True, null=True)
    numero_unidad = models.IntegerField()
    imagen = models.ImageField(upload_to='unidades/', null=True, blank=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='unidades')

    def __str__(self):
        return self.nombre


class Leccion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    numero_leccion = models.IntegerField()
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='lecciones')

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    imagen = models.ImageField(upload_to='usuarios/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Progreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='progresos')
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='progresos')

    class Meta:
        unique_together = ('usuario', 'leccion')

    def __str__(self):
        return f"Progreso de {self.usuario} en {self.leccion}"


class PaginaLeccion(models.Model):
    numero_pagina = models.IntegerField()
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='paginas')

    def __str__(self):
        return f"Página {self.numero_pagina} - {self.leccion.nombre}"


class ContenidoPagina(models.Model):
    texto = models.TextField()
    pagina_leccion = models.ForeignKey(PaginaLeccion, on_delete=models.CASCADE, related_name='contenidos')
    numero_contenido_pagina = models.IntegerField()

    def __str__(self):
        return f"Contenido {self.numero_contenido_pagina} - {self.pagina_leccion}"


class ImagenPagina(models.Model):
    imagen = models.ImageField(upload_to='paginas/')
    pagina_leccion = models.ForeignKey(PaginaLeccion, on_delete=models.CASCADE, related_name='imagenes')
    numero_imagen_pagina = models.IntegerField()

    def __str__(self):
        return f"Imagen {self.numero_imagen_pagina} - {self.pagina_leccion}"


class Pregunta(models.Model):
    texto = models.TextField()
    pagina_leccion = models.ForeignKey(PaginaLeccion, on_delete=models.CASCADE, related_name='preguntas')
    numero_pregunta = models.IntegerField()

    def __str__(self):
        return self.texto


class OpcionPregunta(models.Model):
    texto = models.TextField()
    es_correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')

    def __str__(self):
        return self.texto


class ImagenPregunta(models.Model):
    nombre = models.CharField(max_length=255)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='imagenes')
    numero_imagen_pregunta = models.IntegerField()

    def __str__(self):
        return self.nombre