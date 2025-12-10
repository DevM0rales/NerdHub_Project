import os
import django
import unittest
from unittest.mock import patch, MagicMock
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nerdhub.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from nucleo.models import Produto, Marca, Categoria, Carrinho, ItemCarrinho, Review, Estoque
from usuarios.models import Perfil
from django.core.files.uploadedfile import SimpleUploadedFile

class NerdHubTestCase(TestCase):
    def setUp(self):
        """Set up test dependencies"""
        # Clean up any existing test data first
        User.objects.filter(username='testuser').delete()
        User.objects.filter(username='newuser').delete()
        Marca.objects.filter(nome='Marvel').delete()
        Categoria.objects.filter(nome='Action Figures').delete()
        
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        
        # Create test profile
        self.perfil, created = Perfil.objects.get_or_create(user=self.user)
        
        # Create test brand and category
        self.marca, created = Marca.objects.get_or_create(nome='Marvel')
        self.categoria, created = Categoria.objects.get_or_create(nome='Action Figures')
        
        # Create test client
        self.client = Client()
        
    def tearDown(self):
        """Clean up after tests"""
        # Clean up in reverse order of creation to avoid foreign key issues
        ItemCarrinho.objects.filter(carrinho__usuario=self.user).delete()
        Carrinho.objects.filter(usuario=self.user).delete()
        Review.objects.filter(usuario=self.user).delete()
        Produto.objects.filter(marca=self.marca).delete()
        Perfil.objects.filter(user=self.user).delete()
        User.objects.filter(id=self.user.id).delete()
        Marca.objects.filter(id=self.marca.id).delete()
        Categoria.objects.filter(id=self.categoria.id).delete()

    def test_homepage_loads(self):
        """Test that the homepage loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_about_page_loads(self):
        """Test that the about page loads successfully"""
        response = self.client.get('/sobre/')
        self.assertEqual(response.status_code, 200)
        
    def test_support_page_loads(self):
        """Test that the support page loads successfully"""
        response = self.client.get('/suporte/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()