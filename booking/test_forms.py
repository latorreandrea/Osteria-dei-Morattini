from django.test import TestCase
from .forms import ReservationForm

class TestReservationForm(TestCase):
    
    def test_reservation_slot_is_required(self):
        form = ReservationForm({'party_size': ''})
        self.asserFalse(form.is_valid())
        self.assertIn('party_size', form.errors.keys())
        self.asserEqual(form.errors['name'][0], 'This field is required.')

    
    def test_date_slot_is_required(self):
        form = ReservationForm({'date': ''})
        self.asserFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.asserEqual(form.errors['name'][0], 'This field is required.')

    
    def test_date_slot_is_required(self):
        form = ReservationForm({'time': ''})
        self.asserFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.asserEqual(form.errors['name'][0], 'This field is required.')