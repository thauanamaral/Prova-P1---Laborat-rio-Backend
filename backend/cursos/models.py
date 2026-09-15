from django.db import models
from usuarios.models import Usuario


class Curso(models.Model):
    # Relacionamento 1:N: um usuário pode criar muitos cursos, e cada curso pertence a um único usuário.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cursos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()
    categoria = models.CharField(max_length=80)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
