from django.urls import path
from .views import DashboardView
from .views import BloodTypeCheckAPIView


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('blood-type-check/', BloodTypeCheckAPIView.as_view(), name='blood_type_check_api'),
    
]
