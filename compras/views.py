from django.shortcuts import render, redirect
from django.http import HttpResponse

#from . import models, forms
from .models import Categoria, Compras
from .forms import *

# Create your views here.
def index(request):
    compras = Compras.objects.all()

    return render(request, "compras/index.html", {"compras": compras})

def crear(request):
    if request.method == "POST":
        form = ComprasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("compras:index")
    else:
        form = ComprasForm()
    return render(request, "compras/crear.html", {"form": form})


def buscar(request):
    resultados = []

    if request.method == 'POST':
        form = BuscarPorCategoria(request.POST)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            try:
                categoria = Categoria.objects.get(categoria=categoria)
                resultados = Compras.objects.filter(categoria_id=categoria)
            except Compras.DoesNotExist:
                resultados = []
    
    else:
        form = BuscarPorCategoria()

    return render(request, 'compras/buscar.html', {'form': form, 'resultados': resultados})
