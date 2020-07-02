from django.db.models import Sum
from rest_framework import serializers

from src.models import Bill, BillDetail
from .customer_serializer import CustomerSerializer
from .table_serializer import TableSerializer


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        read_only_fields = ['id']
        fields = '__all__'


class BillDetailMoreSerializer(serializers.ModelSerializer):
    table = TableSerializer()
    customer = CustomerSerializer()
    bill_detail = serializers.SerializerMethodField('get_bill_detail', read_only=True)
    total = serializers.SerializerMethodField('get_total', read_only=True)

    class Meta:
        model = Bill
        fields = '__all__'

    def get_bill_detail(self, obj):
        queryset = BillDetail.objects.values('food', 'food__name', 'food__price') \
            .order_by('food').annotate(amount=Sum('amount_complete')).filter(bill=obj.id)
        print(queryset)
        bill_detail = BillTotalSerializer(queryset, many=True)
        return bill_detail.data

    def get_total(self, obj):
        queryset = BillDetail.objects.filter(bill=obj.id).values('food', 'food__name', 'food__price') \
            .order_by('food').annotate(amount=Sum('amount_complete'))
        total = 0
        for i in queryset:
            total = total + i['food__price'] * i['amount']
        obj.total_money = total
        obj.save()
        return total


class BillTotalSerializer(serializers.ModelSerializer):
    food__name = serializers.CharField(max_length=50)
    amount = serializers.IntegerField()
    food__price = serializers.IntegerField()

    class Meta:
        model = Bill
        fields = ('food__name', 'amount', 'food__price')


class BillDetailTableSerializer(serializers.ModelSerializer):
    table = TableSerializer()

    class Meta:
        model = Bill
        fields = '__all__'
