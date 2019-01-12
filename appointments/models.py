from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Appointment(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    location_name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    due_time = models.DateField()
    member = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
