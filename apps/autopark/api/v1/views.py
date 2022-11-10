from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.autopark.models import Category, Car
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

def test_api_view(request):
    first_Category = Category.objects.first()
    f_b = {
        'title': first_Category.title,
        'is_active': first_Category.is_active,
    }
    return JsonResponse(f_b)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Category_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CategorySerializer(instance=Category.objects.all(), many=True).data, status=200)
        else:
            the_Category = get_object_or_404(Category, pk=pk)
            return Response(data=CategorySerializer(instance=the_Category).data, status=200)
    
    elif request.method == "POST":
        sb = CategorySerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Category = get_object_or_404(Category, pk=pk)
        sb = CategorySerializer(data=request.data, instance=the_Category)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Category = get_object_or_404(Category, pk=pk)
        the_Category.delete()
        return Response('Deleted', status=200)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def test_api_view(request):
    first_Car = Car.objects.first()
    f_b = {
        'title': first_Car.titke,
        'image':first_Car.image,
        'category': first_Car.category,
        'description': first_Car.description,
        'date_create': first_Car.date_create,
    }
    return JsonResponse(f_b)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Car_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CarSerializer(instance=Car.objects.all(), many=True).data, status=200)
        else:
            the_Car = get_object_or_404(Car, pk=pk)
            return Response(data=CarSerializer(instance=the_Car).data, status=200)
    
    elif request.method == "POST":
        sb = CarSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Car = get_object_or_404(Car, pk=pk)
        sb = CarSerializer(data=request.data, instance=the_Car)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Car = get_object_or_404(Car, pk=pk)
        the_Car.delete()
        return Response('Deleted', status=200)


class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    parser_classes = (FormParser, MultiPartParser)


class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDestroyAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

