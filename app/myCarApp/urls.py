from django.conf.urls import url
from myCarApp import views

urlpatterns = [
    url('', views.index, name='index')
]
