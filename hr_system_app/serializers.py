__author__ = 'Cynthia'

from rest_framework import serializers

from hr_system_app.models import *


class CompanySerializer(serializers.ModelSerializer):
	class Meta():
		model = Company
		fields = ('company_name', 'phone_number', 'user_id')
		# exclude = ('user',)
		# fields = '__all__'

	# def get_field_names(self, *args, **kwargs):
	# 	field_names = self.context.get('fields', None)
	# 	if field_names:
	# 		return field_names

	# 	return super(CompanySerializer, self).get_field_names(*args, **kwargs)