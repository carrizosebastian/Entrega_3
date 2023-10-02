from django import forms

from . import models

class ComprasForm(forms.ModelForm):
    class Meta:
        model = models.Compras
        fields = ["articulo", "precio", "cantidad", "categoria_id"]

class BuscarPorCategoria(forms.Form):
    categoria = forms.CharField(label='Buscar por categoria', max_length=100)

