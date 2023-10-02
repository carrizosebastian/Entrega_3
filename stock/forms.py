from django import forms

from . import models

class StockForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ["articulo", "precio", "peso", "cantidad", "ubicacion_id"]

class BuscarPorUbicacion(forms.Form):
    ubicacion = forms.CharField(label='Buscar por ubicacion', max_length=100)

