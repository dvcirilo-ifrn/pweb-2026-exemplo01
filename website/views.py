from django.shortcuts import render
from .models import Prato

def index(request):
    return render(request, 'website/index.html')

def pratos(request):
    pratos = Prato.objects.all()
    context = {"pratos": pratos}
    return render(request, 'website/pratos.html', context)

def sobre(request):
    return render(request, 'website/sobre.html')
