import random

from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def about(request):
    return render(request, 'generator/about.html')


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    generated_password = ''
    # generated_password = ''.join([random.choice(
    #     string.ascii_letters + string.digits + string.punctuation) for n in range(12)])

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'): #aca valido si es mayuscula lo que esta marcado en el formulario de home
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))#se recorre toda la lista
    if request.GET.get('special'):#aca coloco si esta seleccionada la casilla de caracteres especiales
        characters.extend(list('!@#$%&*$'))
    if request.GET.get('numbers'):#aca agrego numeros y etc
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 14))

    for x in range(length):
        generated_password += random.choice(characters)
    return render(request, 'generator/password.html',{'password':generated_password})
