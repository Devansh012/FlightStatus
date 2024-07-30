from django.shortcuts import render
from .models import Flight
from django.http import JsonResponse

def home(request):
    return render(request, 'status/index.html')

def flight_status(request):
    flights = list(Flight.objects.values())
    return JsonResponse(flights, safe=False)
