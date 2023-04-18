from django.db import models

# Create your models here.

class Mapping(models.Model):
    SensorID = models.OneToOneField("api.sensor", on_delete=models.CASCADE)
    UserID = models.ForeignKey("registration.user", on_delete=models.CASCADE)
    vname = models.CharField(max_length=255)
    vnumber = models.CharField(max_length=255)
    status = models.CharField(default="NULL", max_length=255)

