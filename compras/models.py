from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.categoria


class Compras(models.Model):
    articulo = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.articulo} {self.precio} {self.cantidad} {self.categoria_id}"
