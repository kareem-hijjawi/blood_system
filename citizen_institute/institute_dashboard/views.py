from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Citizen
from .serializers import CitizenSerializer
import json


class InstituteDashboardView(TemplateView):
    template_name = "institute_dashboard/dashboard.html"


@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for testing (not recommended in production)
class FilterCitizensView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            city = data.get("city", "").strip()
            address = data.get("address", "").strip()
            blood_type = data.get("blood_type", "").strip()

            # Use Django ORM to filter the Citizen model
            citizens = Citizen.objects.filter(
                city__icontains=city, 
                address__icontains=address, 
                blood_type=blood_type
            ).values("first_name", "last_name", "city", "address", "blood_type", "phone_number")

            return JsonResponse(list(citizens), safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"successful": "valid !"}, status=400)
