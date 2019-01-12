from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import datetime
from appointments.models import Appointment


class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'title',
            'description',
            'address',
            "geolocation",
            'due_time'
        ]


class AppointmentChangeForm(forms.ModelForm):
    """
    This is for members
    """
    class Meta:
        model = Appointment
        fields = (
            'title',
            'description',
            'address',
            "geolocation",
            'due_time'
        )

