"""app URL Configuration

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
from myCarApp import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('lessees/', views.lessees, name='lessees'),
    path('lessors/', views.lessors, name='lessors'),
    path('lessee_register/',views.lessee_registration,name='lessee_register'),
    path('lessor_register/',views.lessor_registration,name='lessor_register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('car_register/', views.car_registration, name='car_register'),
    path('find_car/', views.find_car, name='find_car'),
    path('successful_rent/', views.successful_rent, name='successful_rent'),
    url('myCarApp/', include('myCarApp.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
