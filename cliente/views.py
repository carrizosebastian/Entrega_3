from django.shortcuts import render, redirect
from django.http import HttpResponse

#from . import models, forms
from .models import Cliente
from .forms import *


def index(request):
    clientes = Cliente.objects.all()

    return render(request, "cliente/index.html", {"clientes": clientes})

def crear(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})

def eliminar_cliente(request):
    if request.method == "POST":
        form = EliminarCliente(request.POST)
        if form.is_valid():
            cliente_id = form.cleaned_data['cliente_id']
            try:
                cliente = Cliente.objects.get(pk=cliente_id)
                cliente.delete()
                return redirect("cliente:index")
            except Cliente.DoesNotExist:
                #return HttpResponse("ID de cliente invalido")
                form.add_error('cliente_id', 'ID de cliente inválido. Vuelve a intentarlo.')
    else:
        form = EliminarCliente()
    return render(request, "cliente/eliminar_cliente.html", {"form": form}) 
        


