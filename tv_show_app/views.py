from django.shortcuts import render, redirect
from .models import Canal, Programa
import datetime

def index(request):
    return redirect('/programas')

def programas(request):
    all_programas = {
        "programas": Programa.objects.all()
    }
    return render(request, 'programas.html',all_programas)

def displayprograma(request, programa_id):
    un_programa = {
        "programa": Programa.objects.filter(id=programa_id)
    }
    return render(request, 'programa.html', un_programa)

def editar(request, programa_id):
    un_programa = {
        "programa": Programa.objects.filter(id=programa_id)
    }
    return render(request, 'editar.html', un_programa)

def actualizar(request, programa_id):
    if request.method == "POST":
        programa_actualizado = Programa.objects.get(id=programa_id)
        programa_actualizado.titulo = request.POST['titulo']
        programa_actualizado.estreno = request.POST['estreno']
        programa_actualizado.descripcion = request.POST['descripcion']
        programa_actualizado.updated_at = datetime.datetime.now()
        canal_actualizado = request.POST['canal']
        if Canal.objects.filter(nombre=canal_actualizado).exists():
            programa_actualizado.canal = Canal.objects.get(nombre=canal_actualizado)
        else:
            Canal.objects.create(nombre=canal_actualizado)
            programa_actualizado.canal = Canal.objects.get(nombre=canal_actualizado)
        programa_actualizado.save()
        return redirect('/programas/' + str(programa_id))

def nuevo(request):
    return render(request, 'nuevo.html')

def crear(request):
    if request.method == "POST":
        tit = request.POST['titulo']
        est = request.POST['estreno']
        desc = request.POST['descripcion']
        canal_actualizado = request.POST['canal']
        if Canal.objects.filter(nombre=canal_actualizado).exists():
            canalinput = Canal.objects.get(nombre=canal_actualizado)
        else:
            Canal.objects.create(nombre=canal_actualizado)
            canalinput = Canal.objects.get(name=canal_actualizado)
        Programa.objects.create(titulo=tit,estreno=est,descripcion=desc,canal=canalinput,updated_at=datetime.datetime.now())
        programa_id = Programa.objects.get(titulo=tit)
        return redirect('/programas/'+str(programa_id.id))

def eliminar(request, programa_id):
    elimina = Programa.objects.get(id=programa_id)
    elimina.delete()
    return redirect('/programas')

