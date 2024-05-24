from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.create(
            codigo='CT01',descricao='Curso Teste 01',nivel='B'
        )
        self.curso_02 = Curso.objects.create(
            codigo='CT02',descricao='Curso Teste 02',nivel='I'
        )

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_um_curso(self):
        """Teste para verificar a requisição GET para listar um curso"""
        #/cursos/1/
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        #print(dados_estudante_serializados)
        self.assertEqual(response.data,dados_curso_serializados)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        dados = {
            'codigo':'CTT3',
            'descricao':'Curso teste 3',
            'nivel':'A'
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)