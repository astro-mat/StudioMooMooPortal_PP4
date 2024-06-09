from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    ArtistName = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    BookingRequirements = models.CharField(max_length=700)

    def __str__(self):
        return self.ArtistName
