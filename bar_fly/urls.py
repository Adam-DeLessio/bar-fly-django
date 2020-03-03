from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
	url(r'^ingredients/$', views.IngredientList, name='IngredientList'),
]



urlpatterns = format_suffix_patterns(urlpatterns)