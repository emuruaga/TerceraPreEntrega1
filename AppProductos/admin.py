from django.contrib import admin
from .models import Yerba, Mate, Bombilla, Bolso

class YerbaAdmin(admin.ModelAdmin):
    list_display=['nombre','tamanio']
    search_fields=['nombre', 'tamanio']
    list_filter=['nombre']


# Register your models here.
admin.site.register(Yerba, YerbaAdmin)

admin.site.register(Mate)

admin.site.register(Bombilla)

admin.site.register(Bolso)