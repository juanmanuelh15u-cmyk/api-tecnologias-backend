from django.urls import path
from . import views 

urlpatterns = [
    path ('', views.inicio),
    path ('api/estado/', views.estado),
    path ('api/tecnologias/<int:id>/', views.detalle_tecnologia),
]