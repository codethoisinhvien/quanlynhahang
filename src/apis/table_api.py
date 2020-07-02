from django.db.models import Q
from rest_framework.views import APIView, Response

from src.models import Table, Bill
from src.serializers.bill_serializer import TableSerializer, BillDetailMoreSerializer
from src.serializers.table_serializer import TableUpdateSerializer


class TablesApi(APIView):
    def post(self, request):
        table_serializer = TableSerializer(data=request.data)
        if table_serializer.is_valid():
            table_serializer.save()
            return Response({"success": True, "table": table_serializer.data})
        else:
            return Response({"success": False, "message": table_serializer.error_messages})

    def get(self, request):
        status = request.GET.get('status', None)
        if status is None:
            status_filter = Q()
        else:
            status_filter = Q(status=status)

        tables = Table.objects.filter(status_filter)
        tables_serializer = TableSerializer(tables, many=True)
        return Response({'success': True, 'data': tables_serializer.data})

    def put(self, resquest, id=None):
        table_serializer = TableUpdateSerializer(data=resquest.data)
        if table_serializer.is_valid():
            obj = Table.objects.get(pk=id)
            table_serializer.update(obj, table_serializer.validated_data)
            return Response({"success": True, "message": "ok"})

        else:
            return Response({"success": False, "message": table_serializer.errors})

    def delete(self, request):

        table = Table.objects.get(pk=id).delete()
        return Response({'success': True, 'message': "Xóa thành công"})


class TableApi(APIView):
    def get(self, request, table_id=None):
        bills = Bill.objects.filter(table=table_id,status="OR").first()
        bill_serializer = BillDetailMoreSerializer(bills)
        return Response({'success': True, 'data': bill_serializer.data})
