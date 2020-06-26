from rest_framework import serializers

from src.models import BillDetail


class BillDetailSerializer(serializers.ModelSerializer):
    food_name = serializers.SerializerMethodField('get_food_name', read_only=True)
    price = serializers.SerializerMethodField('get_food_price', read_only=True)

    class Meta:
        model = BillDetail
        fields = ("food_name","amount_complete","price")

    def get_food_name(self, obj):
        return obj.food.name

    def get_food_price(self, obj):
        return obj.food.price
