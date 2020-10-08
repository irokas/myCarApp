# Generated by Django 2.1 on 2020-09-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarApp', '0019_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesseeprofile',
            name='average_cc',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('ABARTH', 'Abarth'), ('ALFA ROMEO', 'Alfa Romeo'), ('AUDI', 'Audi'), ('BMW', 'BMW'), ('CHEVROLET', 'Chevrolet'), ('CITROEN', 'Citroen'), ('DAIHATSU', 'Daihatsu'), ('FIAT', 'Fiat'), ('HONDA', 'Honda'), ('HYUNDAI', 'Hyundai'), ('JEEP', 'Jeep'), ('LANCIA', 'Lancia'), ('LAND ROVER', 'Land Rover'), ('MAZDA', 'Mazda'), ('MERCEDES', 'Mercedes'), ('MINI', 'Mini'), ('MITUBISHI', 'Mitsubishi'), ('NISSAN', 'Nissan'), ('OPEL', 'Opel'), ('PEUGEOT', 'Peugeot'), ('RENAULT', 'Renault'), ('SEAT', 'Seat'), ('SKODA', 'Skoda'), ('SMART', 'Smart'), ('SUZIKI', 'Suzuki'), ('TOYOTA', 'Toyota'), ('VOLKSWAGEN', 'Volkswagen'), ('VOLVO', 'Volvo')], max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('BLACK', 'Black'), ('BLUE', 'Blue'), ('BROWN', 'Brown'), ('GOLD', 'Gold'), ('GREY', 'Grey'), ('RED', 'Red'), ('SILVER', 'Silver'), ('WHITE', 'White'), ('YELLOW', 'Yellow')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuelType',
            field=models.CharField(choices=[('GASOLINE', 'Gasoline'), ('DIESEL', 'Diesel'), ('GAS', 'Gas'), ('ELECTRIC', 'Electric'), ('HYBRID', 'Hybrid')], max_length=10),
        ),
    ]
