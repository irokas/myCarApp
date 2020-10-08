from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myCarApp.forms import UserForm, LesseeForm, CarRegistrationForm
from myCarApp.models import LesseeProfile, LessorProfile, Car
from django.db.models.expressions import F
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.db.models import Count, Sum, FloatField, Func
from django.urls import reverse
import datetime as dt
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def userType(request):
    if hasattr(request.user, "lesseeprofile"):
        type="lessee"
    elif hasattr(request.user, "lessorprofile"):
        type="lessor"
    else:
        type="none"
    return type

def index(request):
    type=userType(request)
    tomorrow = dt.date.today() + dt.timedelta(days=1)
    context={'username':request.user.username,'type':type,'title':"myCar", 'today':dt.date.today(), 'tomorrow':tomorrow}
    return render(request, 'myCarApp/index.html', context)

def lessees(request):
    type=userType(request)

    context={'username':request.user.username,'type':type,'title':"myCar"}
    return render(request, 'myCarApp/lessees.html', context)

def lessors(request):
    type=userType(request)

    context={'username':request.user.username,'type':type,'title':"myCar"}
    return render(request, 'myCarApp/lessors.html', context)

def lessee_registration(request):
    registered=False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        lessee_form = LesseeForm(request.POST,request.FILES)

        if user_form.is_valid() and lessee_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            lessee = lessee_form.save(commit=False)
            lessee.user = user
            if 'driving_license' in request.FILES:
                lessee.driving_license = request.FILES['driving_license']

            lessee.save()

            registered = True
        else:
            print("Error in lessee registration")
            print(user_form.errors, lessee_form.errors)

    else:
        user_form = UserForm()
        lessee_form = LesseeForm()

    return render(request,'myCarApp/lessee_registration.html',
                          {'user_form':user_form,
                           'lessee_form':lessee_form,
                           'registered':registered})


def lessor_registration(request):
    registered=False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            lessor = LessorProfile()
            lessor.user = user
            lessor.save()
            registered = True
        else:
            print("Error in lessor registration")
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'myCarApp/lessor_registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            context={'error': 'Wrong login details, please try again'}
            return render(request,'myCarApp/login.html',context)

    else:
        return render(request, 'myCarApp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def car_registration(request):
    car_is_registered = False
    if request.method == 'POST':
        car_registration_form = CarRegistrationForm(request.POST, request.FILES)

        if car_registration_form.is_valid():
            car = car_registration_form.save()
            car.save()
            car_is_registered = True
        else:
            print("Error in car registration")
            print(car_registration_form.errors)

    else:
        car_registration_form = CarRegistrationForm()
    type=userType(request)
    context={'username': request.user.username, 'type':type,'title':"Car Registration", 'car_registration_form':car_registration_form, 'car_is_registered':car_is_registered}
    return render(request,'myCarApp/car_registration.html',context)

@login_required
def find_car(request):
    searchResult = Car.objects.all()
    if request.method == 'POST':
        firstDay = request.POST.get('firstDay')
        lastDay = request.POST.get('lastDay')
        CC = request.POST.get('CC')
        year = request.POST.get('Year')
        fuelType = request.POST.get('fuelType')
        pricePerDay = request.POST.get('pricePerDay')
        Transmission = request.POST.get('Transmission')

        searchResult = Car.objects.filter(firstAvailableDay__lte=firstDay)
        searchResult = searchResult.filter(lastAvailableDay__gte=lastDay)

        if CC == '500-1000':
            print("500-1000")
            searchResult = searchResult.filter(CC__gte=500).filter(CC__lte=1000)
        elif CC == '1000-1500':
            print("1000-1500")
            searchResult = searchResult.filter(CC__gte=1000).filter(CC__lte=1500)
        elif CC == '1500-2000':
            print("1500-2000")
            searchResult = searchResult.filter(CC__gte=1500).filter(CC__lte=2000)
        elif CC == '2000+':
            print("2000+")
            searchResult = searchResult.filter(CC__gt=2000)

        if year == '1990-1999':
            print("1990-1999")
            searchResult = searchResult.filter(year__gte=1990).filter(year__lte=1999)
        elif year == '2000-2005':
            print("2000-2005")
            searchResult = searchResult.filter(year__gte=2000).filter(year__lte=2005)
        elif year == '2006-2010':
            print("2006-2010")
            searchResult = searchResult.filter(year__gte=2006).filter(year__lte=2010)
        elif year == '2011-2015':
            print("2011-2015")
            searchResult = searchResult.filter(year__gte=2011).filter(year__lte=2015)
        elif year == '2016+':
            print("2016+")
            searchResult = searchResult.filter(year__gte=2016)

        if fuelType == 'Gasoline':
            print("Gasoline")
            searchResult = searchResult.filter(fuelType='GASOLINE')
        elif fuelType == 'Diesel':
            print("Diesel")
            searchResult = searchResult.filter(fuelType='DIESEL')
        elif fuelType == 'Gas':
            print("Gas")
            searchResult = searchResult.filter(fuelType='GAS')
        elif fuelType == 'Electric':
            print("Electric")
            searchResult = searchResult.filter(fuelType='ELECTRIC')

        if pricePerDay == '10-15':
            print("10-15")
            searchResult = searchResult.filter(pricePerDay__gte=10).filter(pricePerDay__lte=15)
        elif pricePerDay == '15-20':
            print("15-20")
            searchResult = searchResult.filter(pricePerDay__gte=15).filter(pricePerDay__lte=20)
        elif pricePerDay == '20-25':
            print("20-25")
            searchResult = searchResult.filter(pricePerDay__gte=20).filter(pricePerDay__lte=25)
        elif pricePerDay == '25+':
            print("25+")
            searchResult = searchResult.filter(pricePerDay__gte=25)

        if Transmission == 'Auto':
            print("Auto")
            searchResult = searchResult.filter(transmission='AUTO')
        elif Transmission == 'Manual':
            print("Manual")
            searchResult = searchResult.filter(transmission='MANUAL')
    currentLessee = LesseeProfile.objects.filter(user=request.user).first()
    currentAverageCc = currentLessee.average_cc
    print(currentAverageCc)
    searchResult = searchResult.annotate(
        averagegap = Func(ExpressionWrapper(F('CC') - currentAverageCc, output_field=FloatField()), function='ABS')
    )

    searchResult = searchResult.order_by('averagegap','pricePerDay','-year')

    type=userType(request)

    if(firstDay>lastDay):
            searchResult=Car.objects.none()
    if(not searchResult):
        message = "Your search returned no results"
    else:
        message = ""
    print(message)
    print(searchResult)

    context={'username': request.user.username, 'type':type,'title':"Find Car",'searchResult':searchResult, 'firstDay': firstDay, 'lastDay': lastDay, 'CC': CC, 'year': year, 'fuelType': fuelType, 'pricePerDay': pricePerDay, 'Transmission': Transmission, 'Message': message}
    return render(request, 'myCarApp/find_car.html', context)


@login_required
def successful_rent(request):
    CC = int(request.POST.get('CC'))
    currentLessee = LesseeProfile.objects.filter(user=request.user).first()
    currentLessee.average_cc = (currentLessee.average_cc*currentLessee.cars_count + CC)
    currentLessee.cars_count = currentLessee.cars_count + 1
    currentLessee.average_cc = currentLessee.average_cc/currentLessee.cars_count
    currentLessee.save()

    firstDay = request.POST.get('firstDay');
    firstDay = datetime.strptime(firstDay, '%Y-%m-%d')
    carId = request.POST.get('carId');
    currentCar = Car.objects.filter(id=carId).first()
    currentCar.firstAvailableDay = firstDay + dt.timedelta(days=1)
    currentCar.save()
    context={'username': request.user.username}
    return render(request, 'myCarApp/successful_rent.html', context)


def base(request):
    type=userType(request)
    context={'username':request.user.username,'type':type}
    return render(request, 'myCarApp/base.html', context)
