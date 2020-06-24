from rest_framework import serializers

from src.models import ChefBill


class ChefBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefBill
        fields = '__all__'
