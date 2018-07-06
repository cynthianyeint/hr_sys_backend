import os,django

def populate():
	admin_group = add_group('Admin')
	staff_group = add_group('Staff')

	company_user = add_user(username='testcompany@gmail.com',
		email='testcompany@gmail.com',
		password='test@1234',
		group=admin_group)

	staff_user = add_user(username='teststaff@gmail.com',
		email='teststaff@gmail.com',
		password='test@1234',
		group=staff_group)

	company = add_company(company_name='testcompany', 
		phone_number='1234',
		user=company_user)

	add_staff(user=staff_user, company=company,
		title='mrs.',
		first_name='test',
		last_name='staff',
		dob='1993-2-14',
		mobile_number='12345678',
		home_phone_number='87654321')

def add_group(name):
	group = Group.objects.get_or_create(name=name)[0]
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
	company = Company.objects.get_or_create(company_name=company_name,phone_number=phone_number,user=user)[0]
	return company

def add_staff(user,company,title,first_name,last_name,dob,mobile_number,home_phone_number):
	staff = Staff.objects.get_or_create(user=user,company=company,title=title,first_name=first_name,last_name=last_name,dob=dob,mobile_number=mobile_number,home_phone_number=home_phone_number)[0]
	return staff


# Start execution here!
if __name__ == '__main__':
    print ("Starting HR system population script...")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hr_system.settings")
    django.setup()

    from django.contrib.auth.models import User, Group
    from hr_system_app.models import *

    from  django.contrib.auth.hashers import *
    
    populate()

