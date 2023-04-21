from django.shortcuts import render , redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Sensor, SensorData
from landing_page.models import Mapping

# Create your views here.
def stats(request):
    if(not is_logged_in(request)):
        redirect("/login")

    id = request.GET.get("id")
    sensor = Sensor.objects.filter(SensorID=id).first()
    mapping = Mapping.objects.filter(SensorID=sensor).first()
    data = SensorData.objects.filter(SensorID=sensor)
    latest_stats = SensorData.objects.filter(SensorID=sensor).order_by("DateTime").first()
    print(latest_stats)
    status = process_sensor_data(data)

    context = {
        "latest_stats" : latest_stats,
        "sensor": sensor,
        "mapping": mapping,
        "status": status
    }
    return render(request,'stats.html', context) 

def is_logged_in(request):
    user = request.user
    return user.is_authenticated


def process_sensor_data(data):
    if(len(data) >= 50):
        data = data[:50]
    required = 0
    not_required = 0
    for entry in data:
        if(entry.Result == 0):
            not_required+=1
        else:
            required+=1  
    if(required >= not_required):
        return "Required"
    else:
        return "Not Required"

# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self,request,format=None):
#         labels= ['January', 'February', 'March', 'April', 'May', 'June', 'July']
#         chartLabel = "my data"
#         chartdata = [0, 10, 5, 2, 20, 30, 45]
#         data={
#                      "labels":labels,
#                      "chartLabel":chartLabel,
#                      "chartdata":chartdata,
#              }
#         return Response(data)