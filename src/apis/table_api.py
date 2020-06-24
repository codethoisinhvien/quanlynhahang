from rest_framework.views import APIView, Response

from src.models import Table
from src.serializers.table_serializer import TableSerializer, TableUpdateSerializer


class TableApi(APIView):
    def post(self, resquest):
        table_serializer = TableSerializer(data=resquest.data)
        if table_serializer.is_valid():
            table_serializer.save()
            return Response({"success": True, "table": table_serializer.data})
        else:
            return Response({"success": False, "message": table_serializer.error_messages})

    def get(self, resquest):
        status=resquest.GET.get('status', None)
        if status==None:
            status= True
        tables = Table.objects.filter(status=status)
        tables_serializer = TableSerializer(tables, many=True)
        return Response({'success': True, 'data': tables_serializer.data})

    def put(self, resquest, id=None):
        table_serializer = TableUpdateSerializer(data=resquest.data)
        if table_serializer.is_valid():
            object = Table.objects.get(id)
            table_serializer.update(object, table_serializer.validated_data)
        else:
            return Response({"success": False, "message": table_serializer.error_messages})

    def delete(self, request):

        table = Table.objects.get(pk=id).delete()
        return Response({'success': True, 'message': "Xóa thành công"})
