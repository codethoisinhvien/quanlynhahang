from typing import re

from rest_framework.views import APIView, Response

from src.models import Bill,Table,Customer
from src.serializers.bill_serializer import BillSerializer, BillDetailMoreSerializer


class BillsAPI(APIView):

    def post(self, request):
        print(request.data)
        table=Table.objects.get(pk=request.data['table'])
        if table.status:
            table.status=False
            table.save()
        else:
            return Response({'success': False, 'message': "Bàn đã được đặt"})
        bill_serializer = BillSerializer(data=request.data)
        if bill_serializer.is_valid():

            bill_serializer.save()
            return Response({'success': True, 'bill': bill_serializer.data})
        else:
            return Response({'success': False, 'message': BillSerializer.errors})

    def get(self, request):
        bill = Bill.objects.filter()
        bill_serializer = BillSerializer(bill, many=True)
        return Response({'success': True, 'bills': bill_serializer.data})




class BillAPI(APIView):
    def get(self, request, id=None):
        bill_detail = Bill.objects.get(pk=id)
        bill_serializer = BillDetailMoreSerializer(bill_detail)
        return Response({
            'success': True,
            'bill': bill_serializer.data
        })

    def put(self, request, id=None):
        bill = Bill.objects.get(pk=id)
        bill.status = request.data["status"]
        if request.data["status"]=="PA":
            bill.table.status=True
            bill.table.save()
        try:
            bill.save()
            bill_serializer = BillDetailMoreSerializer(bill)
            return Response({
                'success': True,
                'message': "Thành công",
                'data': bill_serializer.data
            })
        except:
            return Response({
                'success': False,
                'message': "Thất bại"
            })
