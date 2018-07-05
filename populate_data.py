import os,django

def populate():
	admin_group = add_group('Admin')

	test_user = add_user(username='testcompany@gmail.com',
		email= 'testcompany@gmail.com',
		password='test@1234',
		group=admin_group)

	add_company(company_name='testcompany', 
		phone_number='1234',
		user=test_user)

def add_group(name):
	group = Group.objects.create(name=name)
	return group

def add_user(username,email,password,group):
	user = None
	if User.objects.filter(username=username).exists():
		user = User.objects.get(username=username)
	else:
		user = User()
		user.username = username 
		user.email = username
		user.password = make_password("staffpw@1234", salt=None, hasher='default')
		user.is_active = True
		user.group = group
		user.save()

	return user

def add_company(company_name,phone_number,user):
	# company = None
	# if Company.objects.filter(company_name=company_name).exists():
	# 	company = Company.objects.get(company_name=company_name)
	# else:
	# 	company = Company()
	# 	company.company_name = company_name
	# 	company.phone_number = phone_number
	# 	company.user = user
	# 	company.save()
	company = Company.objects.get_or_create(company_name=company_name,phone_number=phone_number,user=user)[0]

	return company


# Start execution here!
if __name__ == '__main__':
    print "Starting HR system population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hr_system.settings")
    django.setup()

    from django.contrib.auth.models import User, Group
    from hr_system_app.models import *

    from  django.contrib.auth.hashers import *
    
    populate()