from django.urls import path
from .views import InstituteDashboardView, FilterCitizensView

urlpatterns = [
    path('dashboard/', InstituteDashboardView.as_view(), name='institute_dashboard'),
    path("filter_citizens/", FilterCitizensView.as_view(), name="filter_citizens"),
]
