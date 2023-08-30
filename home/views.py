from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from home.models import Car
from home.serializers import CarSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view()
def home(request):
    return Response({'message': "APIs for Tesla Application"})

@api_view(['GET'])
def cars(request):
    try:
        cars = list(Car.objects.all().values())
    except:
        pass

    if request.method == 'GET':
        return JsonResponse(cars, safe=False)
    
    
@api_view(['GET'])
def car(request, id):
    try:
        car = get_object_or_404(Car, id=id) 
    except:
        pass

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
@api_view(['GET'])
def search(request, query):
    try:
        cars = list(Car.objects.filter(title__icontains=query).values())
    except:
        pass

    if request.method == 'GET':
        return JsonResponse(cars, safe=False)