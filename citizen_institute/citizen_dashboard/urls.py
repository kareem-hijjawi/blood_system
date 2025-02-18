from django.urls import path
from .views import DashboardView
from .views import BloodTypeCheckAPIView
from institute_dashboard.models import UrgentCaseList
from .views import UrgentCaseListAPIView, UrgentListView



urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('blood-type-check/', BloodTypeCheckAPIView.as_view(), name='blood_type_check_api'),
    path("api/urgent-cases/", UrgentCaseListAPIView.as_view(), name="urgent_cases_api"),
    path("urgent-cases/", UrgentListView.as_view(), name="urgent_cases_list"),
    
]
