__author__ = 'Cynthia'

from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hr_system_app.models import *

from hr_system_app.serializers import *


@api_view(['GET'])
def company_list(request):
	if request.method == 'GET':
		company_list = Company.objects.all()
		print ("**********")
		print (company_list)
		print ("**********")
		serializer = CompanySerializer(company_list)
		print (serializer)
		print ("**********")
		print (serializer.data)
		print ("**********")

	return Response(serializer.data)