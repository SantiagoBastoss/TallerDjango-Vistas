from django.shortcuts import render
from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ml.getMeasurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurements = ml.getMeasurements()
            measurements_dto = serializers.serialize('json', measurements)
            return HttpResponse(measurements_dto, 'application/json')

    if request.method == 'POST':
        measurement_dto = ml.createMeasurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement = ml.getMeasurement(pk)
        measurement_dto = serializers.serialize('json', measurement)
        return HttpResponse(measurement_dto, 'application/json')

    if request.method == 'PUT':
        measurement_dto = ml.updateMeasurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'DELETE':
        deleted_measurement = ml.deleteMeasurement(pk)
        return HttpResponse(ml.getMeasurements(), 'application/json')
