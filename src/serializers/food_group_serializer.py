
from  rest_framework import  serializers
from  src.models import FoodGroup
class FoodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodGroup
        fields = '__all__'

