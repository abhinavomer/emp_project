"""
URL configuration for oems_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_page,name='logout_page'),
    path('employee/',views.employee,name='index'),
    path('view_emp/',views.view_emp,name='view_emp'),
    path('delete-emp/<id>',views.delete_emp,name='delete-emp'),
    path('update-emp/<id>',views.update_emp,name='update-emp'),
    path('see-emp/<id>',views.see_emp,name='see-emp'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
    
urlpatterns+= staticfiles_urlpatterns()