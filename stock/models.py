from django.db import models

class Ubicacion(models.Model):
    ubicacion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ubicacion

class Stock(models.Model):
    articulo = models.CharField(max_length=100)
    precio = models.IntegerField()
    peso = models.IntegerField()
    cantidad = models.IntegerField()
    ubicacion_id = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.articulo
    