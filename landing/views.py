from django.shortcuts import render

# Create your views here.


def index(request):
    saludo = "Hola me llamo Edwin!"
    usuarios = [
        {"nombre":"Edwin","edad":23,"apellidos":"Salgado"},
        {"nombre":"Alfonso","edad":19,"apellidos":"Torres","escolaridad":"licenciatura"},
        {"nombre":"Luis","edad":27,"apellidos":"Perez"},

    ]
    return render(request,"landing/index.html",{
        "greeting":saludo,
        "users":usuarios
        
        })
def agregar(request):
    return render(request,"landing/agregar.html")