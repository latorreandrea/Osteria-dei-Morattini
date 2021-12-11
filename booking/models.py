from django.db import models
import datetime
# Create your models here.


SEATS = ()

TIME = (
    (0, "11.00/12.00"), (1, "12.00/13.00"),
    (2, "13.00/14.00"), (3, "14.00/15.00"),
    (4, "18.00/19.00"), (5, "19.00/20.00"),
    (6, "20.00/21.00"), (7, "21.00/22.00")
    )
STATUS = ((0, "Accepted"), (1, "Denied"))


class Reservation(models.Model):
    guests = models.IntegerField()
    description = models.TextField(blank=True)
    data = models.DateField()