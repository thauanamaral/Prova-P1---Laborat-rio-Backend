from django.urls import path
from .views import listar_cursos

urlpatterns = [
    path('cursos/', listar_cursos, name='listar_cursos'),
]
