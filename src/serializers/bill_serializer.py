from rest_framework import serializers

from src.models import Bill
from .bill_detail_serializer import BillDetailSerializer
from .table_serializer import TableSerializer


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill

    def get_food_name(self, obj):
        return obj.food.name

    fields = '__all__'


class BillDetailMoreSerializer(serializers.ModelSerializer):
    bill_detail = BillDetailSerializer(many=True)
    table = TableSerializer()

    class Meta:
        model = Bill
        fields = '__all__'
