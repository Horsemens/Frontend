from django.db import models

# Create your models here.

class Mapping(models.Model):
    SensorID = models.ForeignKey("api.sensor", on_delete=models.CASCADE, unique=True)
    UserID = models.ForeignKey("registration.user", on_delete=models.CASCADE)
    vname = models.CharField(max_length=255)
    vnumber = models.CharField(max_length=255)

