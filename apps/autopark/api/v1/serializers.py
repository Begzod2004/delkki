from rest_framework import serializers
from apps.autopark.models import Category, Car


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
