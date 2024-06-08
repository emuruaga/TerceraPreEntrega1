from django.urls import path
from AppProductos.views import (
    yerba, lista_yerbas, inicio,
    yerbas, mates, Bombillas,bolsos,
    yerba_formulario,mate_formulario,
    busqueda_mate, buscar_material
    )

urlpatterns = [
    path('agrega-yerba/<nombre>/<tamanio>/', yerba, name='yerba'),
    path('lista-yerbas/', lista_yerbas, name='lista_yerbas' ),
    path('', inicio, name='inicio' ),
    path('yerbas/', yerbas, name='yerbas' ),
    path('mates/', mates, name='mates' ),
    path('bombillas/', Bombillas, name='Bombillas' ),
    path('bolsos/', bolsos, name='bolsos' ),
    path('yerba-formulario/', yerba_formulario, name='YerbaFormulario' ),
    path('mate-formulario/', mate_formulario, name='MateFormulario' ),
    path('busqueda-mate/', busqueda_mate, name='BusquedaMate' ),
    path('buscar-material/', buscar_material, name='BuscarMate' ),
]
