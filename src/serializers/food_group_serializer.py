from django.db.models import Q
from rest_framework import serializers

from src.models import FoodGroup, Food
from .food_serializer import FoodSerializer


class FoodGroupSerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField("get_list_food")

    class Meta:
        model = FoodGroup
        fields = '__all__'

    def get_list_food(self, obj):
        # print(obj.id)
        condition = Q(food_group=obj.id)

        food = Food.objects.filter(condition)
        food_serializer = FoodSerializer(food, many=True)
        return food_serializer.data


class FoodGroupUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)

    class Meta:
        model = FoodGroup
        fields = ('name',)
