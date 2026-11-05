from django.shortcuts import render, redirect
from .models import Competidor

def bienvenida(request):
    return render(request, 'senasoft_app/bienvenida.html')

def registro(request):
    if request.method == 'POST':
        nombre_form = request.POST.get('nombre')
        centro_form = request.POST.get('centro')
        categoria_form = request.POST.get('categoria')

        Competidor.objects.create(
            nombre=nombre_form,
            centro=centro_form,
            categoria=categoria_form
        )
        return redirect('competidores')

    return render(request, 'senasoft_app/registro.html')

def competidores(request):
    lista_competidores = Competidor.objects.all()
    return render(request, 'senasoft_app/competidores.html', {'competidores': lista_competidores})