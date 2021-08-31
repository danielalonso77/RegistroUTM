from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado
from .models import Materiales 
from .forms import MaterialesForm

# Create your views here.

def registro(request):
    materiales = Materiales.objects.all()
    data = {
        'materiales': materiales
    }
    return render(request, "inicio/registro.html", data) 

def inicio(request):
    return render(request, "inicio/index.html")

def pricipal(request):
    empleados = Empleado.objects.all()
    return render(request, "inicio/principal.html",{'empleados':empleados})

def formulario(request):
    data ={
        'form ': MaterialesForm()
    }
    if request.method == 'POST':
        form = MaterialesForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"]="Guardado"
            materiales = Materiales.objects.all()
            return render(request, "inicio/registro.html", {'materiales':materiales})
        else:
            data["mensaje"] = "fallo"
    return render(request, "inicio/formulario.html", data)

def editar(request, id):
    
    material = get_object_or_404(Materiales, id=id)
    data = {
        'form': MaterialesForm(instance=material)
    }

    if request.method == 'POST':
        form = MaterialesForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect(to='Registro')
        data["form"]=form  

    return render(request, "inicio/editar.html", data)

def eliminar(request, id):
    material = get_object_or_404(Materiales, id=id)
    material.delete()
    return redirect(to='Registro')
    
