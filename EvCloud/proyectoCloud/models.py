from django.db import models

# Create your models here.
class Tareas(models.Model):
    PRIORIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    prioridad = models.CharField(max_length=5, choices=PRIORIDAD_CHOICES)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
class TareasFinalizadas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    prioridad = models.CharField(max_length=10)
