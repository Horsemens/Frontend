from django.shortcuts import render , redirect
from api.models import Sensor
from registration.models import User
from .models import Mapping
from django.contrib.auth import logout


# Create your views here.
def landing(request):
    if(not is_logged_in(request)):
        redirect("/login")

    current_user = request.user
    current_user_id = current_user.id
    user = User.objects.filter(id=current_user_id).first()

    if request.method == "POST":
        if request.POST.get("logout") and request.POST.get("logout") == "Logout":
            logout(request)
            return redirect("/login")

        
        if not request.user.is_authenticated:
            logout(request)
            return redirect("/login")
        
        
        sensorID = request.POST.get("sensorID")
        vname = request.POST.get("vname")
        vnumber = request.POST.get("vnumber")

        sensor = Sensor.objects.filter(SensorID=sensorID).first()

        status = validate(sensor=sensor, user=user, vname=vname ,vnumber=vnumber)

        msg = ''
        if(status == "sensor err"):
            msg = '<p class="text-danger m-0">Invalid Sensor ID</P> '
        if(status == "user err"):
            logout(request)
            return redirect("/login")
        if(status == "vname err"):
            msg = '<p class="text-danger m-0">Invalid Vehicle Name</P>'
        if(status == "vnumber err"):
            msg = '<p class="text-danger m-0">Invalid Vehicle Number</P>'
        if(status == "valid"):
            msg = '<p class="text-success m-0">Vehicle Added Successfully</p>'
            mapping  = Mapping(UserID=user, SensorID=sensor, vname=vname, vnumber=vnumber)
            try:
                mapping.save()
            except:
                msg = '<p class="text-danger m-0">Invalid Addition Please check SensorID</p>'

        return redirect("." + "?response="+msg)
    
    context = {}
    sensors_owned = Mapping.objects.filter(UserID=user)
    vehicle_names = []
    vehicle_numbers = []

    for i in range(0, len(sensors_owned)):
        vehicle_names.append(sensors_owned[i].vname)
        vehicle_numbers.append(sensors_owned[i].vnumber)
    
    context["vehicle_names"] = vehicle_names
    context["vehicle_numbers"] = vehicle_numbers
    context["vehicles"] = sensors_owned
    context["images"] = ["gUQNKPd.png", "SKZolYE.png", "edOjtEC.png"]

    if(request.GET.get("response")):
        context["response"] = request.GET.get("response")

    return render(request,'landing_page.html', context=context)


def validate(sensor, vname, vnumber, user):
    if(sensor is None):
        return "sensor err"
    if(user is None):
        return "user err"
    if(len(vname) < 1):
        return "vname err"
    if(len(vnumber) < 1):
        return "vnumber err"
    
    return "valid"

def is_logged_in(request):
    user = request.user
    return user.is_authenticated