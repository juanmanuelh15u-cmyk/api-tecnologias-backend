from django.http import HttpResponse, JsonResponse 

TECNOLOGIAS = [
    {"id": 1, "nombre": "Python", "tipo": "lenguaje", "anio": 1991},
    {"id": 2, "nombre": "Django", "tipo": "framework", "anio": 2005},
    {"id": 3, "nombre": "React", "tipo": "Libreria", "anio": 2013},
    {"id": 4, "nombre": "Mysql", "tipo": "base de datos", "anio": 1995},

]

def inicio(requets):
    return HttpResponse ("Hola desde Django. Mi primer servidor con python")

def estado(request):
    return JsonResponse({"servidor": "activo", "framework": "Django"})

def listar_tecnologias(request):
    return JsonResponse(TECNOLOGIAS, safe=False)

def detalle_tecnologia (request, id):
    for tecnologia in TECNOLOGIAS:
        if tecnologia ["id"] == id:
            return JsonResponse(tecnologia)
    return JsonResponse ({"error": f"tecnologia {id} no encontrada"}, status=404)    
