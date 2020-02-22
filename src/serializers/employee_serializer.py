from rest_framework import serializers
from src.models import Emloyee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emloyee
        feilds = '__all__'