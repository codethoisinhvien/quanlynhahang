from rest_framework import serializers

from src.models import Customer


class BillStatisticSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    total_money= serializers.IntegerField()
    total_bill = serializers.IntegerField()
    class Meta:
        model = Customer
        fields = (('date','total_money','total_bill'))
