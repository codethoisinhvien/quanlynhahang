
from  rest_framework import  serializers
from  src.models import FoodGroup
class FoodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodGroup
        fields = '__all__'
class FoodGroupUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)

    class Meta:
        model = FoodGroup
        fields = ('name',)
