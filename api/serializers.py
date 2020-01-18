from rest_framework import serializers
from .models import Patients, Bottles

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ["id","name", "age", "bottle", "disease", "room_number", "bed_number"]

class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model =Bottles
        fields = ["id", "level", "status"]

