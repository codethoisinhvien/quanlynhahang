from rest_framework.views import APIView, Response

from src.models import Table
from src.serializers.table_serializer import TableSerializer, TableUpdateSerializer


class TableApi(APIView):
    def post(self, request):
        table_serializer = TableSerializer(data=request.data)
        if table_serializer.is_valid():
            table_serializer.save()
            return Response({"success": True, "table": table_serializer.data})
        else:
            return Response({"success": False, "message": table_serializer.error_messages})

    def get(self, request):
        status=request.GET.get('status', None)
        if status is None:
            status= True
        tables = Table.objects.filter(status=status)
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
