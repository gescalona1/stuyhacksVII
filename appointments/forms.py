from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings
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
            'latitude',
            "longitude",
            'due_time'
        ]

        class Media:
            if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
                css = {
                    'all': ('css/admin/location_picker.css',),
                }
                js = (
                    f'https://maps.googleapis.com/maps/api/js?key={settings.GOOGLE_MAPS_API_KEY}',
                    'js/admin/location_picker.js'
                )


class AppointmentChangeForm(forms.ModelForm):
    """
    This is for members
    """
    class Meta:
        model = Appointment
        fields = (
            'title',
            'description',
            'latitude',
            "longitude",
            'due_time'
        )
        class Media:
            if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
                css = {
                    'all': ('css/admin/location_picker.css',),
                }
                js = (
                    'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                    'js/admin/location_picker.js',
                )
