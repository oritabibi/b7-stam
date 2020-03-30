from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.http import HttpResponse

app_name = 'dog_gardens'

urlpatterns = [
    url(r'^$', views.dog_garden_list, name='list'),
    url(r'^(?P<name>[\w-]+[0-9]*)/$', views.garden_details),
]
