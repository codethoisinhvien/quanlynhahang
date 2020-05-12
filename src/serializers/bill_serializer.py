from rest_framework import serializers
from django.db.models import Q
from src.models import Bill, Customer
from .bill_detail_serializer import BillDetailSerializer
from .table_serializer import TableSerializer
from .customer_serializer import CustomerSerializer


class BillSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField("get_customer")

    class Meta:
        model = Bill
        fields = ['table', 'customer', 'status']

    def get_customer(self, obj):
        # print(obj.id)
        condition = Q(pk=obj.customer.id)

        customer = Customer.objects.get(pk=obj.customer.id)
        customerS = CustomerSerializer(customer, many=False)
        return customerS.data


class BillDetailMoreSerializer(serializers.ModelSerializer):
    bill_detail = BillDetailSerializer(many=True)
    table = TableSerializer()

    class Meta:
        model = Bill
        fields = '__all__'
