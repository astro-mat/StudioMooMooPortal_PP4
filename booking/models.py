from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=30)
    date = models.DateField()
    booking_requirements = models.CharField(max_length=700)

    def __str__(self):
        return self.artist_name
