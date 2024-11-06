

from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)
    rubro = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
