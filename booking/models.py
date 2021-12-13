from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    time = models.TimeField()
    

    def __str__(self):
        return 'booked for {party} at {time} on {date}, on behalf {name} '.format(
            party=self.party_size,
            time=self.time,
            date=self.date,
            name=self.name
            )
            