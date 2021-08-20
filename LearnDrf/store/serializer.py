# Requirements
from rest_framework import serializers
from .models import Store


# Code
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
