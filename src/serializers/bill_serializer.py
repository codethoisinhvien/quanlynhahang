from rest_framework import serializers
from django.db.models import Q
from src.models import Bill, Customer
from .bill_detail_serializer import BillDetailSerializer
from .table_serializer import TableSerializer
from .customer_serializer import CustomerSerializer


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        read_only_fields = ['id']
        fields = '__all__'



class BillDetailMoreSerializer(serializers.ModelSerializer):
    bill_detail = BillDetailSerializer(many=True)
    table = TableSerializer()

    class Meta:
        model = Bill
        fields = '__all__'
