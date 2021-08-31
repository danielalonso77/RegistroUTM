from django.db import models

# Create your models here.

class Materiales(models.Model):
    nombre = models.CharField( max_length=40, verbose_name='nombre') 
    material = models.CharField( max_length=40, verbose_name='material')
    carrera = models.CharField( max_length=5, verbose_name='carrera')
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
        ordering = ["-created"]
    def __str__(self):
        return self.nombre
        


class Empleado(models.Model):
    nombre = models.TextField() 
    edad = models.CharField(max_length=2) 
    codigo_empleado = models.CharField(max_length=12) 
    imagen= models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    turno = models.TextField()
    created = models.DateTimeField(auto_now_add=True)     #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ["-created"]
    def __str__(self):
        return self.nombre