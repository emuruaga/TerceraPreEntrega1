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

def inicio(req):
    return render(req, 'inicio.html', {}) 

def yerbas(req):
    return render(req, 'yerbas.html', {}) 

def mates(req):
    return render(req, 'mates.html', {}) 

def Bombillas(req):
    return render(req, 'bombillas.html', {}) 

def bolsos(req):
    return render(req, 'bolsos.html', {}) 

def about(req):
    return render(req, 'about.html', {}) 

#formularios
def yerba_formulario(req):
    print('method: ', req.method)
    print('POST: ', req.POST)
    
    if req.method == 'POST':
        nueva_yerba=Yerba(nombre=req.POST['yerba'], tamanio=req.POST['tamanio'])
        nueva_yerba.save()
        return render(req, 'inicio.html', {})
    else:
        return render (req, 'yerba_formulario.html', {})