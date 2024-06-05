from django.http import HttpResponse
from django.shortcuts import render
from .models import Yerba

# Create your views here.
def yerba(req, nombre, tamanio):
    nueva_yerba=Yerba(nombre=nombre, tamanio=tamanio)
    nueva_yerba.save()
    
    return HttpResponse(f'''
         <p>Yerba: {nueva_yerba.nombre} - Tamaño: {nueva_yerba.tamanio} creado!</p>               
                        ''')
    
def lista_yerbas(req):
    lista=Yerba.objects.all()
    return render(req, 'lista_yerbas.html', {'lista_yerbas': lista})    