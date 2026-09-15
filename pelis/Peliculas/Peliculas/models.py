from django.db import models

class Distribuidora(models.Model):
    nombre = models.CharField(max_length=150)
    rubro = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('agotado', 'Agotada'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')

    def save(self, *args, **kwargs):
        if self.cantidad == 0:
            self.estado = 'agotado'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"