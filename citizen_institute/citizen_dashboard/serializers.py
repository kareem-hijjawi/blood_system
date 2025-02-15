from rest_framework import serializers
from .models import KhaldaHospitalAppointment

class KhaldaHospitalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhaldaHospitalAppointment
        fields = '__all__'
