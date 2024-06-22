from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Artist_Name = models.CharField(max_length=30)
    Date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    Booking_Requirements = models.CharField(max_length=700)

    def __str__(self):
        return self.Artist_Name
