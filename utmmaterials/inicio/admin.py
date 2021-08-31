from django.contrib import admin
from .models import Empleado, Materiales

# Register your models here.

class AdministrarMateriales(admin.ModelAdmin):
    list_display=('id','nombre','carrera','material')
    search_fields=('id','created','carrera')
    date_fields='created'
    readonly_fields=('created', 'id')
    list_filter=('nombre', 'material')

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    date_hierarchy = 'created'
    list_filter = ('nombre','turno')
    search_fields=('nombre','edad','imagen','turno','codigo_empleado')
    list_display=('nombre','edad','imagen','turno','codigo_empleado')

admin.site.register(Empleado, AdministrarModelo)
admin.site.register(Materiales, AdministrarMateriales)
