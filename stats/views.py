from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def stats(request):
    return render(request,'stats.html') 

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