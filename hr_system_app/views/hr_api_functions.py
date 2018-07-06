__author__ = 'Cynthia'

from rest_framework import mixins, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from hr_system_app.models import *

from hr_system_app.serializers import *

@api_view(['GET'])
def user_list(request):
	if request.method == 'GET':
		user_list = User.objects.all()
		serializer = UserSerializer(user_list, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def user_detail(request):
	if request.method == 'GET':
		user_id = int(request.META['HTTP_USERID'])
		user_list = User.objects.get(pk=user_id)
		serializer = UserSerializer(user_list, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def company_list(request):
	if request.method == 'GET':
		company_list = Company.objects.all()
		serializer = CompanySerializer(company_list, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def company_detail(request, format=None):
	if request.method == 'GET':
		company_id = int(request.META['HTTP_COMPANYID'])
		company= Company.objects.get(pk=company_id)
		serializer = CompanySerializer(company_list, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def staff_list(request):
	if request.method == 'GET':
		staff_list = Staff.objects.all()
		serializer = StaffSerializer(staff_list, many=True)

	return Response(serializer.data)

