from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto


def agendarHora(request):
    eventos_data = [
        {
            'title': 'Cita de ejemplo',
            'start': '2023-10-10',
            'end': '2023-10-12'
        },
        {
            'title': 'Otra cita de ejemplo',
            'start': '2023-10-15',
            'end': '2023-10-17'
        }
    ]

    return render(request, "pelu/agendarHora.html", {'eventos': eventos_data})

def agregar_evento(request):
    nuevo_evento = {
        'title': request.POST.get('titulo'),
        'start': request.POST.get('start'),
        'end': request.POST.get('end')
    }
    return JsonResponse(nuevo_evento)

def inicio(request):
    context={}

    return render(request, "pelu/inicio.html", context)

def nosotros(request):
    context={}

    return render(request, "pelu/sobreNosotros.html", context)

def login(request):
    context={}
    return render(request, "pelu/iniciarsesion.html", context)



def tienda(request):
    context={}
    return render(request, "pelu/tienda.html", context)