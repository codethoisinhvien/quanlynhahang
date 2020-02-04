from rest_framework.views import APIView, Response

from src.models import Bill
from src.serializers.bill_serializer import BillSerializer


class BillAPI(APIView):

    def post(self, request):
        bill_serializer = BillSerializer(data=request.data)
        if bill_serializer.is_valid():

            bill_serializer.save()
            return Response({'success': True, 'bill': bill_serializer.data})
        else:
            return Response({'success': False, 'message': BillSerializer.data})

    def get(self, request):
        bill = Bill.objects.filter()
        bill_serializer = BillSerializer(bill, many=True)
        return Response({'success': True, 'bills': bill_serializer.data})


