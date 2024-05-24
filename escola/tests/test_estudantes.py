from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)