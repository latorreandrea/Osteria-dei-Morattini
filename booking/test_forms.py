from django.test import TestCase
from datetime import datetime
from .forms import ReservationForm

class TestBookingCreation(TestCase):
    def test_form_is_valid(self):
        """Test that the form is valid"""
        # Use all correct form data
        data = {'party_size': 9, 'date':datetime.now(), 'time':"1"}
        form = ReservationForm(data)
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid(self):
        """Test that the form is not valid"""
        # Use incorrect type of party_size in form
        data = {'party_size': "test", 'date':datetime.now(), 'time':"1"}
        form = ReservationForm(data)
        self.assertFalse(form.is_valid())


