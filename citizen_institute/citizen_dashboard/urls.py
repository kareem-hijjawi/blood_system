from django.urls import path
from .views import DashboardView
from .views import BloodTypeCheckAPIView,BloodDonationAppointmentView


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('blood-type-check/', BloodTypeCheckAPIView.as_view(), name='blood_type_check_api'),
    path('blood_donation/', BloodDonationAppointmentView.as_view(), name='blood_donation_appointment'),
    
]
