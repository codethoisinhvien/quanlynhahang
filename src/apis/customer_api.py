from rest_framework.views import APIView,Response
from src.serializers.customer_serializer import CustomerSerializer
from src.models import Customer
class CustomersAPI(APIView):
    def post(self, request):
        customer_serializer= CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return  Response({'success':True,'customer':customer_serializer.data})
        else:
            return Response({'success': False, 'message': customer_serializer.error_messages})

    def get(self, request):
        pass


class CustomerAPI(APIView):
    def get(self, request, id=None):
        pass

    def put(self, request, id=None):
        pass

    def delete(self, request, id=None):
        pass
