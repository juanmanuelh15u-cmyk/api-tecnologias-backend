from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listar_biblioteca),
    path('libros/<int:id>/', views.detalle_biblioteca),
    path('libros/genero/<str:genero>/', views.libreria_genero),
    path('libros/disponibles/', views.libros_disponibles),
    path('libros/resumen/', views.resumen),
    path('libros/autor/<str:autor>/', views.libros_por_autor),
]