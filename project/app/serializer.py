from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['employee', 'department']

class excelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFields
        fields = ['user_name']