from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula

class MatriculasTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='lais')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)
    
    def test_requisicao_get_para_listar_matriculas(self):
        """Teste para verificar a requisição GET para listar as matriculas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_requisicao_post_para_criar_matricula(self):
        """Teste para verificar a requisição POST para criar uma matrícula"""
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'M'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_nao_deletar_matricula(self):
        """Teste para verificar a requisição DELETE não autorizada para deletar uma matricula"""
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_para_atualizar_matricula(self):
        """Teste para verificar a requisição PUT não permitida para atualizar uma matricula"""
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'V'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)