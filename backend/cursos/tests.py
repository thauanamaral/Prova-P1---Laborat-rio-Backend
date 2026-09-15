from django.test import TestCase

from usuarios.models import Usuario
from .models import Curso


class CursoApiTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nome='Maria Silva',
            email='maria@email.com',
            senha='senha123'
        )
        Curso.objects.create(
            usuario=self.usuario,
            nome='Python para Iniciantes',
            descricao='Curso focado em fundamentos de Python.',
            carga_horaria=40,
        )

    def test_listar_cursos_endpoint(self):
        response = self.client.get('/api/cursos/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['nome'], 'Python para Iniciantes')
