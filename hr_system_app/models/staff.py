__author__ = 'Cynthia'

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from hr_system_app.models import *

TITLE_CHOICES = (
    ('mr.', 'Mr.'),
    ('ms.', 'Ms.'),
    ('mrs.', 'Mrs.'),
    # ('dr.', 'Dr.'),
    # ('prof.', 'Prof.'),
)

class Staff(models.Model):
    title = models.CharField(max_length=20, null=True, blank=False, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    dob = models.DateField(blank=False, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{6,15}$', message="Phone number must be entered in the format: '+999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(max_length=15, validators=[phone_regex], blank=True, null=True)
    home_phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True, null=True)
    user = models.ForeignKey(User, null=False)
    company = models.ForeignKey(Company, null=False, on_delete=models.CASCADE)
    
    @property
    def title_text(self):
        for (k, v) in TITLE_CHOICES:
            if k == self.title:
                return v

        return ""

    def __unicode__(self):
        return ("%s %s %s" % (self.title_text, self.first_name, self.last_name if self.last_name else "")).strip()

    @property
    def get_staff_name(self):
        return ("%s %s %s" % (self.title_text, self.first_name, self.last_name if self.last_name else "")).strip()

    @property
    def get_phone_number(self):
        if self.home_phone_number and self.mobile_number:
            return "%s , %s" % (self.home_phone_number, self.mobile_number)
        elif self.home_phone_number:
            return self.home_phone_number
        elif self.mobile_number:
            return self.mobile_number
        else:
            return "-"

    @property
    def email(self):
        return self.user.email if self.user and self.user.email else "-"

    @property
    def get_date_joined(self):
        return self.user.date_joined.date

    
