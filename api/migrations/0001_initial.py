# Generated by Django 4.1.7 on 2023-04-18 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('SensorID', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('Role', models.CharField(max_length=255)),
                ('Topic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AFRDifference', models.IntegerField(null=True)),
                ('DateTime', models.DateTimeField(null=True)),
                ('BatteryVoltage', models.IntegerField(null=True)),
                ('IgnitionTiming', models.IntegerField(null=True)),
                ('AirTemp', models.IntegerField(null=True)),
                ('CoolantTemp', models.IntegerField(null=True)),
                ('MAPSource', models.IntegerField(null=True)),
                ('RPM', models.IntegerField(null=True)),
                ('LambdaSensor1', models.IntegerField(null=True)),
                ('BaseFuel', models.IntegerField(null=True)),
                ('BaseIgnition', models.IntegerField(null=True)),
                ('Result', models.IntegerField(null=True)),
                ('SensorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sensor')),
            ],
        ),
    ]
