from rest_framework import serializers

from src.models import ChefBill, BillDetail,Bill
from src.serializers.bill_serializer import BillDetailTableSerializer


class ChefBillSerializer(serializers.ModelSerializer):
    bill = serializers.SerializerMethodField("get_bill_detail")

    class Meta:
        model = ChefBill
        fields = '__all__'

    def get_bill_detail(self, obj):

        bill = BillDetailTableSerializer(obj.bill_detail.bill)
        return bill.data
