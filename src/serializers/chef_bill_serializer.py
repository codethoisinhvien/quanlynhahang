from rest_framework import serializers

from src.models import ChefBill, BillDetail,Bill
from src.serializers.bill_serializer import BillDetailTableSerializer


class ChefBillSerializer(serializers.ModelSerializer):
    table = serializers.SerializerMethodField("get_bill_detail")
    food= serializers.SerializerMethodField("get_food_name")
    class Meta:
        model = ChefBill
        fields = (("table","food","id","amount","status","delivery_by"))

    def get_bill_detail(self, obj):

        bill = BillDetailTableSerializer(obj.bill_detail.bill)
        return bill.data['table']['name']
    def get_food_name(self, obj):
        return obj.bill_detail.food.name
