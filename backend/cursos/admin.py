from django.contrib import admin
from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'carga_horaria', 'usuario')
    search_fields = ('nome', 'categoria')