
from  rest_framework import  serializers
from  src.models import BillDetail
class BillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetail
        fields = '__all__'

