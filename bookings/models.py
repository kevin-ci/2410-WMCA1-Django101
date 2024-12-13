from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='bookings', null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_people = models.IntegerField()
    quiet_room = models.BooleanField()
    total_price = models.DecimalField(default=100.00, max_digits=5, decimal_places=2)