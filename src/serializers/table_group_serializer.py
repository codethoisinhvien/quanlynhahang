from rest_framework import serializers

from src.models import TableGroup,Table
from .table_serializer import TableSerializer

class TableGroupSerializer(serializers.ModelSerializer):
    tables = serializers.SerializerMethodField("get_list_table")
    class Meta:
        model = TableGroup
        fields = '__all__'

    def get_list_food(self, obj):
        # print(obj.id)
        food = Table.objects.filter(table_group=obj.id)
        food_serializer = TableSerializer(food, many=True)
        return food_serializer.data

class TableGroupUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = TableGroup
        fields = '__all__'
