from django.db import models
import datetime
# Create your models here.

YEAR = ()
MONTH = ()
DAY = ()
SEATS = ()
TIME = (
    (0, "11.00/12.00"), (1, "12.00/13.00"),
    (2, "13.00/14.00"), (3, "14.00/15.00"),
    (4, "18.00/19.00"), (5, "19.00/20.00"),
    (6, "20.00/21.00"), (7, "21.00/22.00")
    )
STATUS = ((0, "Accepted"), (1, "Denied"))


def default_year():
    return datetime.datetime.now().year


def default_month():
    return datetime.datetime.now().month


def default_day():
    return datetime.datetime.now().day


class Reservation(models.Model):
    year = models.JSONField(default=default_year)
    month = models.IntegerField(default=default_month)
    day = models.IntegerField(default=default_day)
    seats = models.IntegerField(default=1)
    time = models.IntegerField(choices=TIME, default=0)

    class Meta:
        indexes = [
            models.Index(fields=['seats', 'day', 'month', 'year', 'time'])
        ]