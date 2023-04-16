from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
import pickle 
import os
import pandas as pd
import numpy as np
import json
from .models import SensorData , Sensor

# Create your views here.
@csrf_exempt
def insert(request):
    if request.method == 'POST':
        # decode request body
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # create copy to store in database
        data= body.copy()
        # remove this pareameter as they are not part of machine leaning model
        data.pop("DateTime")
        data.pop("SensorId")
        # format data according to machine leaning model input
        data = format_data(data)
        ans = perform_model_operations(data)
        result = { "result" : str(ans) }

        # save params and result to database
        save_to_database(body, ans)

        return JsonResponse(result)
    
    return HttpResponseNotAllowed(permitted_methods=["POST"])


# permoform database operations
def save_to_database(data, ans):
    sensor = Sensor.objects.filter(SensorID=data["SensorId"]).first()
    sensorData = SensorData(
        SensorID = sensor, 
        AFRDifference = float(data["AFRDifference[AFR]"]),
        DateTime = data["DateTime"],
        BatteryVoltage = float(data["BatteryVoltage[BatteryVoltage]"]),
        IgnitionTiming = float(data["IgnitionTiming[Angle]"]),
        AirTemp = float(data["AirTemp[Temperature]"]),
        CoolantTemp = float(data["CoolantTemp[Temperature]"]),
        MAPSource = float(data["MAPSource[Pressure]"]),
        RPM = float(data["RPM[EngineSpeed]"]),
        LambdaSensor1 = float(data["LambdaSensor1[AFR]"]),
        BaseFuel = float(data["BaseFuel[Percentage]"]),
        BaseIgnition = float(data["BaseIgnition[AngleIgnSprt2K]"]),
        Result = ans
    )
    sensorData.save()


# formats data
def format_data(data):
    formated_data = {}
    keys = data.keys()
    for key in keys:
        formated_data[key] = [data[key]]
    return formated_data
        

# perform prediction
def perform_model_operations(data):
    model = load_model()
    df_me = pd.DataFrame(data)
    df_me_f = df_me[data.keys()]
    scaler1 = preprocessing.MinMaxScaler().fit(df_me_f)
    df_me_f_scaled = scaler1.transform(df_me_f)
    ans = model.predict(df_me_f_scaled)
    return ans
    
# loads model from .pkl file
def load_model():
    module_dir = os.path.dirname(__file__)   #get current directory
    file_path = os.path.join(module_dir, 'model.pkl')
    model_pkl = open(file_path, 'rb')     
    model = pickle.load(model_pkl)
    return model