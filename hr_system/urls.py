"""hr_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from hr_system_app import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/user/list/$', views.user_list),
    url(r'^api/v1/user/detail/$', views.user_detail),
    url(r'^api/v1/company/list/$', views.company_list),
    url(r'^api/v1/company/detail/$', views.company_detail)
    url(r'^api/v1/staff/list', views.staff_list)
]