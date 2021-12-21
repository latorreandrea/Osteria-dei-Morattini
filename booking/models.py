from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TIME_CHOICES = (
    ("1", "10.00-11.00"),
    ("2", "11.00-12.00"),
    ("3", "12.00-13.00"),
    ("4", "13.00-14.00"),
    ("5", "19.00-20.00"),
    ("6", "20.00-21.00"),
    ("7", "21.00-22.00"),
    ("8", "22.00-23.00"),    
    )


class Booking(models.Model):
    """
    Bookings need to know:
    - which user booked
    - the number of people
    - the day
    - the time slot
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    party_size = models.PositiveIntegerField()    
    date = models.DateField(null=True)
    time = models.CharField(max_length=100,
                  choices=TIME_CHOICES)
    
    def __str__(self):
        return 'booked for {party} at {time} on {date}, on behalf {name} '.format(
            party=self.party_size,
            time=self.time,
            date=self.date,
            name=self.name
            )