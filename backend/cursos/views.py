from django.http import JsonResponse
from .models import Curso


def listar_cursos(request):
    cursos = Curso.objects.select_related('usuario').all().values(
        'id',
        'nome',
        'descricao',
        'categoria',
        'carga_horaria',
        'usuario__nome',
        'data_cadastro',
    )
    return JsonResponse(list(cursos), safe=False)