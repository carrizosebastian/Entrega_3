from django import forms

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido"]

class EliminarCliente(forms.Form):
    cliente_id = forms.IntegerField(label='ID Cliente')