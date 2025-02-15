from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from rest_framework.views import APIView  
from .models import KhaldaHospitalAppointment


class DashboardView(TemplateView):
    template_name = "citizen_dashboard/cdashboard.html"


class BloodTypeCheckAPIView(APIView):  
    def get(self, request):
        return render(request, "citizen_dashboard/BloodTypeCheck.html")
    
    def post(self, request):
        city = request.POST.get('city')
        hospital = request.POST.get('hospital')
        citizen_name = request.POST.get('citizen_name')
        email = request.POST.get('email')
        appointment_date = request.POST.get('appointment_date')

        if city and hospital and appointment_date and citizen_name and email:
            if hospital == "Khalda Hospital":
                appointment = KhaldaHospitalAppointment.objects.create(
                    city=city,
                    hospital=hospital,
                    citizen_name=citizen_name,
                    email=email,
                    appointment_date=appointment_date
                )
                return JsonResponse({
                    "message": "Your appointment has been reserved successfully!",
                    "appointment": {
                        "id": appointment.id,
                        "city": appointment.city,
                        "hospital": appointment.hospital,
                        "citizen_name": appointment.citizen_name,
                        "email": appointment.email,
                        "appointment_date": str(appointment.appointment_date)
                    }
                }, status=201)
            else:
                return JsonResponse({"error": "Only Khalda Hospital appointments are supported."}, status=400)
        else:
            return JsonResponse({"error": "Please fill all fields."}, status=400)
