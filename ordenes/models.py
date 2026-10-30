from django.db import models

class LibroPrestado(models.Model):
    nombre_persona = models.CharField(max_length=100, verbose_name="Nombre de la persona")
    identificacion = models.CharField(max_length=20, verbose_name="Identificación")
    titulo_libro = models.CharField(max_length=150, verbose_name="Libro prestado")
    fecha_prestamo = models.DateField(auto_now_add=True, verbose_name="Fecha de préstamo")

    def __str__(self):
        return f"{self.nombre_persona} - {self.titulo_libro}"