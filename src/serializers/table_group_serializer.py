from rest_framework import serializers

from src.models import TableGroup


class TableGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableGroup
        fields = '__all__'


class TableGroupUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = TableGroup
        fields = '__all__'
