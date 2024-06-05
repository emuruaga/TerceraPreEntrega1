from django.urls import path
from AppProductos.views import yerba, lista_yerbas, inicio, yerbas, mates, Bombillas,bolsos

urlpatterns = [
    path('agrega-yerba/<nombre>/<tamanio>/', yerba, name='yerba'),
    path('lista-yerbas/', lista_yerbas, name='lista_yerbas' ),
    path('', inicio, name='inicio' ),
    path('yerbas/', yerbas, name='yerbas' ),
    path('mates/', mates, name='mates' ),
    path('bombillas/', Bombillas, name='Bombillas' ),
    path('bolsos/', bolsos, name='bolsos' ),
]
