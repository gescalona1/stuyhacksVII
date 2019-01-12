from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Appointment(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    name_of_location = models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    due_time = models.DateField()
    member = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
