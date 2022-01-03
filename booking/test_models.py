from django.test import TestCase
from .models import Booking
from django.contrib.auth.models import User
from datetime import datetime
from django.test import Client
from django.shortcuts import reverse

class TestModel(TestCase):
    def setUp(self):
        """Setting up testing environment"""
        # Create test user
        user = User.objects.create_user(username="Test", password="testpassword")
        # Create a Booking Object   
        Booking.objects.create(name=user, party_size=8, date=datetime.now(), time="1")

    def test_booking_is_created(self):
        """Test that the reservation created from user is correct"""
        reservation = Booking.objects.get(name=User.objects.filter(username="Test")[0])
        self.assertEqual(reservation.party_size, 8)
        self.assertEqual(reservation.time, "1")

        count = Booking.objects.all().count()
        # Test object in DB size equal 1
        self.assertEqual(count, 1)

    def test_booking_is_deleted(self):
        """Test that the reservation deleted """
        reservation = Booking.objects.get(name=User.objects.filter(username="Test")[0])
        count = Booking.objects.all().count()

        # Test Pre delete check object in DB size equal 1
        self.assertEqual(count, 1)

        # Test reservation object is deleted
        self.assertTrue(reservation.delete())
        count = Booking.objects.all().count()
        # Test Post delete check object in DB size equal 0
        self.assertEqual(count, 0)
