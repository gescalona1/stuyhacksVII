from django.db import models
from django.contrib.auth import get_user_model
from django_google_maps import fields as map_fields
# Create your models here.


class Appointment(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    due_time = models.DateField()
    member = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
