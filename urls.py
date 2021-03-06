"""stutens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from stutens_manage.views import classes,teachers,students, ajax,Login,Host

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes.html', classes.get_classes),
    path('add_classes.html', classes.add_classes),
    path('del_classes.html', classes.del_classes),
    path('edit_classes.html', classes.edit_classes),

    path('students.html', students.get_students),
    path('add_students.html', students.add_students),
    path('del_students.html', students.del_students),
    path('edit_students.html', students.edit_students),

    path('set_teachers.html', classes.set_teachers),
    path('ajax.html', ajax.del_classes),

    path('index.html', Login.index),
    path('log_out.html', Login.log_out),
    path('host.html', Host.host_web)
]
