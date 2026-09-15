from django.db import models


class Certificado(models.Model):
    aluno = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='certificados')
    curso = models.ForeignKey('cursos.Curso', on_delete=models.CASCADE, related_name='certificados')
    codigo = models.CharField(max_length=50, unique=True)
    concluido = models.BooleanField(default=True)
    data_emissao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.curso}"
