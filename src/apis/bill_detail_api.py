from rest_framework.views import APIView, Response

from src.models import BillDetail
from src.serializers.bill_detail_serializer import BillDetailSerializer


class BillDetail(APIView):
    def post(self, request):
        bill_setail_serializer = BillDetailSerializer(data=request.data,many=True)
        if bill_setail_serializer.is_valid():
            bill_setail_serializer.save()
            return Response({"success": True, 'bill_detail': bill_setail_serializer.data})
        else:
            return Response({"success": False, 'bill_detail': bill_setail_serializer.error_messages})

    def put(self, request, id=None):

        bill_setail_serializer = BillDetailSerializer(data=request.data)
        if bill_setail_serializer.is_valid():
            object = BillDetail.objects.get(pk=id)
            bill_setail_serializer.update(object, bill_setail_serializer.validated_data)
            return Response({"success": True, 'bill_detail': bill_setail_serializer.validated_data})
        else:
            return Response({"success": False, 'bill_detail': bill_setail_serializer.error_messages})

    def delete(self, request, id=None):
        object = BillDetail.objects.get(pk=id)
        object.status = False
        object.save()
        return Response({'success': True, 'message': 'Xóa thành công'})

