from rest_framework import serializers

from src.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class FoodUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    status = serializers.BooleanField(default=True)

    class Meta:
        model = Food
        fields = '__all__'
class BestFoodSerializer(serializers.ModelSerializer):
    food__name = serializers.CharField(max_length=50)
    count = serializers.IntegerField()
    count_complete = serializers.IntegerField()
    class Meta:
        model = Food
        fields = (('food__name','count','count_complete'))
