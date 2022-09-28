from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Libro(models.Model):
    libro = models.CharField(max_length=200)

    def __str__(self):
        return self.libro

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    alumno = models.CharField(max_length=200)

    def __str__(self):
        return self.alumno