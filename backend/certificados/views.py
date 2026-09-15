from django.http import JsonResponse
from .models import Certificado


def listar_certificados(request):
    certificados = Certificado.objects.select_related('aluno', 'curso').all().values(
        'id',
        'codigo',
        'concluido',
        'data_emissao',
        'aluno__nome',
        'curso__nome',
    )
    return JsonResponse(list(certificados), safe=False)
