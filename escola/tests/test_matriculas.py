from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula

class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.create(
            nome='Estudante Teste',
            email='estudante@gmail.com',
            cpf='77567543010',
            data_nascimento='2003-02-02',
            celular='11 98765-4321'
        )
        self.curso = Curso.objects.create(
            codigo='CTT',descricao='Curso Teste',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='M'
        )
    
    def test_requisicao_get_para_listar_matriculas(self):
        """Teste para verificar a requisição GET para listar as matriculas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 