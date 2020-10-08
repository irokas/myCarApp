from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class LesseeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    driving_license = models.ImageField(upload_to='driving_licenses', blank=True)
    average_cc = models.FloatField(blank=True, default=0)
    cars_count = models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.user.username

class LessorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    def __str__(self):
        return self.user.username


TRANSMISSION_CHOICES = [('MANUAL','Manual'),('AUTO','Auto'),]

FUEL_CHOICES = [('GASOLINE','Gasoline'),('DIESEL','Diesel'),('GAS','Gas'),('ELECTRIC','Electric'),('HYBRID','Hybrid'),]

YEAR_CHOICES = [(i,i) for i in range(1990,2020)]

BRAND_CHOICES = [('ABARTH', 'Abarth'),('ALFA ROMEO', 'Alfa Romeo'),('AUDI', 'Audi'),('BMW','BMW'),('CHEVROLET', 'Chevrolet'),('CITROEN','Citroen'),('DAIHATSU','Daihatsu'),('FIAT','Fiat'),('HONDA','Honda'),('HYUNDAI','Hyundai'),('JEEP','Jeep'),('LANCIA','Lancia'),('LAND ROVER','Land Rover'),('MAZDA','Mazda'),('MERCEDES','Mercedes'),('MINI','Mini'),('MITUBISHI','Mitsubishi'),('NISSAN','Nissan'),('OPEL','Opel'),('PEUGEOT','Peugeot'),('RENAULT','Renault'),('SEAT','Seat'),('SKODA','Skoda'),('SMART','Smart'),('SUZIKI','Suzuki'),('TOYOTA','Toyota'),('VOLKSWAGEN','Volkswagen'),('VOLVO','Volvo'),]

COLOR_CHOICES = [('BLACK','Black'),('BLUE','Blue'),('BROWN','Brown'),('GOLD','Gold'),('GREY','Grey'),('RED','Red'),('SILVER','Silver'),('WHITE','White'),('YELLOW','Yellow'),]

class Car(models.Model):
    brand = models.CharField(max_length = 30, choices=BRAND_CHOICES)
    model = models.CharField(max_length = 30)
    CC = models.IntegerField()
    year = models.IntegerField(choices=YEAR_CHOICES, default=2020)
    color = models.CharField(max_length = 10, choices=COLOR_CHOICES)
    transmission = models.CharField(max_length = 10, choices=TRANSMISSION_CHOICES)
    fuelType = models.CharField(max_length = 10, choices=FUEL_CHOICES)
    firstAvailableDay = models.DateField()
    lastAvailableDay = models.DateField()
    pricePerDay = models.FloatField()
    photo = models.ImageField(upload_to='car_photos')

