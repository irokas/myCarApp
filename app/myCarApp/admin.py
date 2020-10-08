from django.contrib import admin
from myCarApp.models import LesseeProfile, LessorProfile,User, Car

# Register your models here.
admin.site.register(LesseeProfile)
admin.site.register(LessorProfile)
admin.site.register(Car)
