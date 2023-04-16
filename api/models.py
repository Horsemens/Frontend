from django.db import models

# Create your models here.
class SensorData(models.Model):
    SensorID = models.ForeignKey("sensor", on_delete = models.CASCADE)
    AFRDifference = models.IntegerField(null=True)
    DateTime = models.DateTimeField(null=True)
    BatteryVoltage = models.IntegerField(null=True)
    IgnitionTiming = models.IntegerField(null=True)      
    AirTemp = models.IntegerField(null=True)
    CoolantTemp = models.IntegerField(null=True)
    MAPSource = models.IntegerField(null=True)
    RPM = models.IntegerField(null=True)
    LambdaSensor1 = models.IntegerField(null=True) 
    BaseFuel = models.IntegerField(null=True)
    BaseIgnition = models.IntegerField(null=True)
    Result = models.IntegerField(null=True)

class Sensor(models.Model):
    SensorID = models.CharField(max_length=255, unique=True, primary_key=True)
    Role = models.CharField(max_length=255)
    Topic = models.CharField(max_length=255)

