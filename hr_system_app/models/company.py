__author__ = 'Cynthia'

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Company(models.Model): 
	company_name = models.CharField(max_length=200, null=False, blank=True, default="")
	user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
	phone_regex = RegexValidator(regex=r'^\+?1?\d{6,15}$', message="Phone number must be entered in the format: '+999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True, null=True)
	
	def __unicode__(self):
		return self.name

	@property
	def get_email(self):
		return self.user.email

	@property
	def get_date_joined(self):
		return self.user.date_joined.date
