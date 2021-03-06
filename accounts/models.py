from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import MemberManager
import datetime
# Create your models here.


class Member(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        help_text= None,
        unique=True,
        max_length=20)
    email = models.CharField(
        _('email'),
        help_text=None,
        unique=True,
        max_length=40)
    first_name = models.CharField(
        _('first name'),
        help_text=None,
        max_length=30)
    last_name = models.CharField(
        _('last name'),
        help_text=None,
        max_length=30)
    date_of_birth = models.DateField(
        _('date of birth'),
        help_text=None)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = MemberManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def age(self):
        today = datetime.datetime.utcnow()
        age = today - self.date_of_birth
        return age

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

