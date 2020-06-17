from rest_framework import serializers

from src.models import Customer


class BillStatisticSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    total= serializers.IntegerField()
    class Meta:
        model = Customer
        fields = (('date','total'))
