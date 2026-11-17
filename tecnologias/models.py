from django.db import models


class Tecnologia(models.Model):
    CATEGORIAS = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('base_datos', 'Base de datos'),
        ('movil', 'Móvil'),
        ('devops', 'DevOps'),
        ('ia', 'Inteligencia Artificial'),
        ('ciberseguridad', 'Ciberseguridad'),
        ('cloud', 'Cloud Computing'),
        ('qa', 'Control de Calidad (QA)'),
        ('iot', 'Internet de las Cosas (IoT)'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS)
    descripcion = models.TextField(blank=True)
    anio_creacion = models.PositiveIntegerField()
    sitio_web = models.URLField(blank=True)
    activa = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Tecnología'
        verbose_name_plural = 'Tecnologías'

    def __str__(self):
        return self.nombre
