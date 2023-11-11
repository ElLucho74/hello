from django.shortcuts import render

# Create your views here.
# mi_app/views.py
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo en DJango Atte. El TSU de Iztapalapa para el mundo Luis Castrooooo!")
