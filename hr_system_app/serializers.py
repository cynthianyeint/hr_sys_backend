__author__ = 'Cynthia'

from rest_framework import serializers
from django.contrib.auth.models import User
from hr_system_app.models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta():
		model = User
		# fields = ('company_name', 'phone_number', 'user_id')
		# exclude = ('user',)
		fields = '__all__'

	def get_field_names(self, *args, **kwargs):
		field_names = self.context.get('fields', None)
		if field_names:
			return field_names

		return super(UserSerializer, self).get_field_names(*args, **kwargs)

class CompanySerializer(serializers.ModelSerializer):
	class Meta():
		model = Company
		# fields = ('company_name', 'phone_number', 'user_id')
		# exclude = ('user',)
		fields = '__all__'

	def get_field_names(self, *args, **kwargs):
		field_names = self.context.get('fields', None)
		if field_names:
			return field_names

		return super(CompanySerializer, self).get_field_names(*args, **kwargs)

class StaffSerializer(serializers.ModelSerializer):
	class Meta():
		model = Staff
		fields = '__all__'

	def get_field_names(self, *args, **kwargs):
		field_names = self.context.get('fields', None)
		if field_names:
			return field_names

		return super(StaffSerializer, self).get_field_names(*args, **kwargs)
