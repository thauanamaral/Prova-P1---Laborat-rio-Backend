from django.contrib import admin
from .models import Certificado


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'aluno', 'curso', 'concluido', 'data_emissao')
    search_fields = ('codigo', 'aluno__nome', 'curso__nome')