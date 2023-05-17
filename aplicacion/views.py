from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'usuario.html')

def reserva(request):
    return render(request, 'reserva-de-salas.html')

def menu(request):
    return render(request, 'menu_principal.html')

def implementos(request):
    return render(request, 'implementos.html')

def cliente(request):
    return render(request, 'cliente.html')

def canchas(request):
    return render(request, 'canchas.html')

def canchas2(request):
    return render(request, 'cancha-usuario.html')

def Login(request):
    return render(request, 'login.html')