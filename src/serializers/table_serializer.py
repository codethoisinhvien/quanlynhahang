from rest_framework import serializers

from src.models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
class TableUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50),
    class Meta:
        model = Table
        fields = '__all__'

