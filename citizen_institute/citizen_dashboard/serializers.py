from rest_framework import serializers
<<<<<<< HEAD
from .models import KhaldaHospitalAppointment,BloodDonationAppointment
=======
from .models import KhaldaHospitalAppointment
from institute_dashboard.models import UrgentCaseList
>>>>>>> 3f828d538dede124e70f60cde78393f1375e4e2d

class KhaldaHospitalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhaldaHospitalAppointment
        fields = '__all__'


<<<<<<< HEAD

class BloodDonationAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= BloodDonationAppointment
        fields= '__all__'
        
    def validate(self, data):
        """
        Custom validation to ensure:
        - Users who donated in the last 2 months can't donate now.
        - Donation units can only be selected if donation is allowed.
        """
        if data.get('donated_last_two_months'):
            raise serializers.ValidationError("You cannot donate now. Please wait at least 2 months.")
        
        if not data.get('donated_last_two_months') and not data.get('donation_units'):
            raise serializers.ValidationError("Please select the number of donation units.")

        return data
=======
class UrgentCaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrgentCaseList
        fields = "__all__"
>>>>>>> 3f828d538dede124e70f60cde78393f1375e4e2d
