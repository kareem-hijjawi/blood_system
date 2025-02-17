from django.urls import path
from .views import DashboardView
<<<<<<< HEAD
from .views import BloodTypeCheckAPIView,BloodDonationAppointmentView
=======
from .views import BloodTypeCheckAPIView
from institute_dashboard.models import UrgentCaseList
from .views import UrgentCaseListAPIView, UrgentListView

>>>>>>> 3f828d538dede124e70f60cde78393f1375e4e2d


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('blood-type-check/', BloodTypeCheckAPIView.as_view(), name='blood_type_check_api'),
<<<<<<< HEAD
    path('blood_donation/', BloodDonationAppointmentView.as_view(), name='blood_donation_appointment'),
=======
    path("api/urgent-cases/", UrgentCaseListAPIView.as_view(), name="urgent_cases_api"),
    path("urgent-cases/", UrgentListView.as_view(), name="urgent_cases_list"),
>>>>>>> 3f828d538dede124e70f60cde78393f1375e4e2d
    
]
