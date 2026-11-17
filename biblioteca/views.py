import unicodedata
from django.http import JsonResponse

LIBROS = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "genero": "novela", "anio": 1967, "disponible": True},
    {"id": 2, "titulo": "La vorágine", "autor": "José Eustasio Rivera", "genero": "novela", "anio": 1924, "disponible": False},
    {"id": 3, "titulo": "Python Crash Course", "autor": "Eric Matthes", "genero": "tecnologia", "anio": 2019, "disponible": True},
    {"id": 4, "titulo": "Clean Code", "autor": "Robert C. Martin", "genero": "tecnologia", "anio": 2008, "disponible": False},
    {"id": 5, "titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "genero": "novela", "anio": 1985, "disponible": True},
    {"id": 6, "titulo": "Breve historia de Colombia", "autor": "Jorge Orlando Melo", "genero": "historia", "anio": 2017, "disponible": True},
    {"id": 7, "titulo": "Sapiens", "autor": "Yuval Noah Harari", "genero": "historia", "anio": 2011, "disponible": False},
    {"id": 8, "titulo": "Django for Beginners", "autor": "William S. Vincent", "genero": "tecnologia", "anio": 2022, "disponible": True},
]

def _normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def listar_biblioteca(request):
    return JsonResponse(LIBROS, safe=False)

def detalle_biblioteca(request, id):
    for libros in LIBROS:
        if libros["id"] == id:
            return JsonResponse(libro)
    return JsonResponse({"error": "Libro no encontrado"}, status=404)

def libreria_genero (request, genero):
    resultado = []
    for libro in LIBROS:
        if libro["genero"] == genero:
            resultado = resultado + [libro]
    return JsonResponse(resultado, safe=False)

def libros_disponibles(request):
    resultado = []
    for libro in LIBROS:
        if libro["disponible"] == True:
            resultado = resultado + [libro]
    return JsonResponse(resultado, safe=False)

def resumen(request):
    total = len(LIBROS)
    disponibles = 0
    for libro in LIBROS:
        if libro["disponible"] == True:
            disponibles = disponibles + 1
    prestados = total - disponibles
    return JsonResponse({"total": total, "disponibles": disponibles, "prestados": prestados})


def libros_por_autor(request, autor):
    resultado = []
    for libro in LIBROS:
        if autor in libro["autor"]:
            resultado = resultado + [libro]
    return JsonResponse(resultado, safe=False)


        



