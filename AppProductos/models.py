from django.db import models

# Create your models here.
class Yerba(models.Model):
    nombre=models.CharField(max_length=30)
    tamanio=models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} - {self.tamanio}'
    
class Mate(models.Model):
    tipo=models.CharField(max_length=30)
    material=models.CharField(max_length=30)
    
    def  __str__(self):
        return f'{self.tipo} - {self.material}'
    
class Bombilla(models.Model):
    tipo=models.CharField(max_length=30)
    material=models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.tipo} - {self.material}'
    
class Bolso(models.Model):
    material=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.material} - {self.color}'