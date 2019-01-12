from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import datetime


class MemberCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'date_of_birth', 'password',
        ]
        widgets = {
            'email': forms.TextInput(attrs={
                'style': 'text-transform:lowercase;'
            }),
            'password': forms.PasswordInput()
        }


class MemberChangeForm(forms.ModelForm):
    """
    This is for admins
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'date_of_birth', 'is_active')

    def clean_password(self):
        return self.initial["password"]


class MemberLogForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={
                'style': 'text-transform:lowercase;'
            }),
            'password': forms.PasswordInput()
        }
