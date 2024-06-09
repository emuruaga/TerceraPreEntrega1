from django.http import HttpResponse
from django.shortcuts import render
from .models import Yerba
from .models import Mate
from .models import Bolso
from .forms import MateFormulario, BolsoFormulario

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

#Formularios

def yerba_formulario(req):
    print('method: ' , req.method)
    print('POST: ' , req.POST)
    
    if req.method=='POST':   
        nueva_yerba=Yerba(nombre=req.POST['yerba'], tamanio=req.POST['tamanio'])
        nueva_yerba.save()
        return render(req, 'inicio.html', {}) #Acá poner otra página que diga agregado correctamente!!!!!       
    else:
        return render(req, 'yerba_formulario.html', {}) #Ver vien la url, cuál es la q invoca!!!
    
    
def mate_formulario(req):
    print('method: ' , req.method)
    print('POST: ' , req.POST)
    
    if req.method=='POST':
        miFormulario=MateFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
        
            nuevo_mate=Mate(tipo=data['tipo'], material=data['material'])
            nuevo_mate.save()
            return render(req, 'mates.html', {'messege': 'Curso creado con éxito'}) #Acá poner otra página que diga agregado correctamente!!!!!      
        else:
            return render(req, 'mate_formulario.html', {'messege': 'Datos inválidos'})
    else:
        miFormulario=MateFormulario()
        return render(req, 'mate_formulario.html', {'miFormulario': miFormulario})
    
#Busquedas en los formularios    
    
def busqueda_mate(req):
    return render(req, 'busqueda_mate.html', {})

def buscar_material(req):
    material = req.GET.get('material')
    if material:
        mates = Mate.objects.filter(material=material)
        if mates.exists():
            return render(req, 'resultadoBusqueda.html', {'mates': mates, 'material': material})
        else:
            return render(req, 'inicio.html', {'messege': 'No se encontraron resultados para el material especificado'})
    else:
        return render(req, 'inicio.html', {'messege': 'No es correcto el dato'})
'''def buscar_material(req):
    
    if req.GET['material']:
        material=req.GET['material']
        mate=Mate.objects.get(material=material)
        return render (req, 'resultadoBusqueda.html', {'mate': mate, 'material': material})
    else:
        return render(req, 'inicio.html',{'messege': 'No es correcto el dato'})'''
#Leer registro
def lista_bolsos(req):
    mis_bolsos=Bolso.objects.all()
    return render(req, 'leer_bolsos.html', {'bolsos': mis_bolsos})

#Crear Registros
def crea_bolso(req):
    if req.method=='POST':
        miFormulario=BolsoFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
        
            nuevo_bolso=Bolso(material=data['material'], color=data['color'])
            nuevo_bolso.save()
            return render(req, 'bolsos.html', {'messege': 'Nuevo bolso creado con éxito'}) #Acá poner otra página que diga agregado correctamente!!!!!      
        else:
            return render(req, 'bolso_formulario.html', {'messege': 'Datos inválidos'})
    else:
        miFormulario=BolsoFormulario()
        return render(req, 'bolso_formulario.html', {'miFormulario': miFormulario})
    
#Eliminar registros
def eliminar_bolso(req, id):
    if req.method=='POST':
        bolso=Bolso.objects.get(id=id)
        bolso.delete()
        mis_bolsos=Bolso.objects.all()
    return render(req, 'leer_bolsos.html', {'bolsos': mis_bolsos})

#Editar un registro
def editar_bolso(req,id):
    
    if req.method=='POST':
        miFormulario=BolsoFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            bolso=Bolso.objects.get(id=id)
            bolso.material=data['material']
            bolso.color=data['color']
            bolso.save()
        
            return render(req, 'bolsos.html', {'messege': 'Bolso modificado con éxito'}) #Acá poner otra página que diga agregado correctamente!!!!!      
        else:
            return render(req, 'bolso_formulario.html', {'messege': 'Datos inválidos'})
    else:
        bolso=Bolso.objects.get(id=id)
        miFormulario=BolsoFormulario(initial={
            'material': bolso.material,
            'color': bolso.color
        })
        return render(req, 'editar_bolso.html', {'miFormulario': miFormulario, 'id': bolso.id})
    