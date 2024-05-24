from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste estudante UM',
            email = 'testeestudante01@gmail.com',
            cpf ='68224431002',
            data_nascimento='2024-01-02',
            celular = '86 99999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste estudante DOIS',
            email = 'testeestudante02@gmail.com',
            cpf ='70261486055',
            data_nascimento='2024-01-02',
            celular = '86 99999-9999'
        )
    
    def test_requisicao_get_para_listar_estudantes(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)#/estudantes/
        self.assertEqual(response.status_code,status.HTTP_200_OK)