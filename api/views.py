from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FormParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from datetime import datetime, timezone
from django.shortcuts import redirect

from .models import Patients, Bottles, BottleStats
from .serializers import PatientSerializer, BottleSerializer
# Create your views here.

@csrf_exempt
def get_bottle_info(request, pk):
    try:
        bottle_info = Bottles.objects.get(pk=pk)
    except Bottles.DoesNotExist:
        return HttpResponse(status=404)

    serializer = BottleSerializer(bottle_info)
    return JsonResponse(serializer.data)
    

@csrf_exempt
def get_patients_list(request):
    print(request.method)
    if request.method == 'GET':
        level_status = {}
        patients = Patients.objects.all()


        print(patients)
        serializer = PatientSerializer(patients, many=True)

        print(serializer.data)

        return JsonResponse(serializer.data, safe=False)
        #return Response(patient_info, status=status.HTTP_201_CREATED)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def update_bottle_level(request, pk):

    try:
        bottle = Bottles.objects.get(pk=pk)
        update_bottle_stats(request, pk)
    except Bottles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "POST":
        data = FormParser().parse(request)
        serializer = BottleSerializer(bottle, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return redirect("get_patients_list")
        return JsonResponse(serializer.errors, status=400)

def get_bottle_drip_rate_utility(initial_time, final_time):

    total_time = final_time-initial_time
    total_time = total_time.total_seconds()
    return 25/(total_time)

def get_bottle_drip_rate(pk, current_time) :
    all_stats = BottleStats.objects.filter(bottle_primary_key=pk)
    try:
        previous_time = all_stats[len(all_stats)-1].timestamp
        rate = get_bottle_drip_rate_utility(previous_time, current_time)
    except:
        rate = 0
    return rate

def update_bottle_stats(request, pk):
    level = request.POST["level"]
    current_time = datetime.now(timezone.utc)
    rate = get_bottle_drip_rate(pk, current_time)
    BottleStats.objects.create(bottle_primary_key=pk, level=level, timestamp=current_time, rate=rate)




