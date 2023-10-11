from django import forms

from . import models

class StockForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = "__all__"

        widgets = {
            "articulo": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "peso": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad": forms.TextInput(attrs={"class": "form-control"}),
            "ubicacion_id.name": forms.TextInput(attrs={"class": "form-control"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class BuscarPorUbicacion(forms.Form):
    ubicacion = forms.ModelChoiceField(queryset=models.Ubicacion.objects.all(),label='Buscar por ubicacion', widget=forms.Select(attrs={'class': 'form'}))

