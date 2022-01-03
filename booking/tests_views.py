from django.test import TestCase
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from .models import Booking
from datetime import datetime
from django.contrib.auth.models import User
from .forms import ReservationForm
from django.test import Client


class TestViews(TestCase):
    def setUp(self):
        """Setting up testing environment"""
        # Create test user
        user = User.objects.create_user(username="Test", password="testpassword")

    def test_homepage_correct_loading(self):
        """Test booking insert request response code is 200 - correct response"""
        c = Client()
        response = c.get('//')
        self.assertEqual(response.status_code, 200)

    def test_correct_login_and_redirect(self):
        """Test Login request response code is 200 - correct response"""
        c = self.client
        user_login = c.login(username="Test", password="testpassword")
        self.assertTrue(user_login)
        
        resp = c.get(reverse('index'), follow=True)

        # Check if user is logged in
        self.assertEquals(str(resp.context['user']), 'Test')
        # Check if response is "success"
        self.assertEqual(resp.status_code, 200)
        
        # Test correct template is used
        self.assertTemplateUsed(resp, 'index.html')

    def test_correct_myreservation_redirect(self):
        """Test booking insert request response code is 200 - correct response"""
        c = self.client
        user_login = c.login(username="Test", password="testpassword")
        
        data = {'party_size': "test", 'date':datetime.now(), 'time':"1"}
        form = ReservationForm(data)
        
        # Reverse to myreservation
        resp = c.get(reverse('reservations'), follow=True)

        # Check if response is "success"
        self.assertEqual(resp.status_code, 200)
        
        # Test correct template is used
        self.assertTemplateUsed(resp, 'reservations.html')