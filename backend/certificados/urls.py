from django.urls import path
from .views import listar_certificados

urlpatterns = [
    path('certificados/', listar_certificados, name='listar_certificados'),
]
