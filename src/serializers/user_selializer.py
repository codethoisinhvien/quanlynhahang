from rest_framework import serializers

from src.models import User


class UserSerializer(serializers.ModelSerializer):
    office_name = serializers.SerializerMethodField('get_office')

    class Meta:
        model = User
        fields = '__all__'

    def get_office(self, obj):
        return obj.office.name
