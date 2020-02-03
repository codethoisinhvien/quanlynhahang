from rest_framework.views import APIView, Response

from src.serializers.table_serializer import TableSerializer,TableUpdateSerializer
from src.models import Table

class TableApi(APIView):
    def post(self, resquest):
        table_serializer = TableSerializer(data=resquest.data)
        if table_serializer.is_valid():
            table_serializer.save()
            return Response({"success": True, "table": table_serializer.data})
        else:
            return Response({"success": False, "message": table_serializer.error_messages})
    def get(self, resquest):
        tables= Table.objects.all()
        tables_serializer = TableSerializer(tables ,many=True)
        return Response({'success': True, 'data':  tables_serializer.data})

    def put(self, resquest,id=None):
        table_serializer = TableUpdateSerializer(data=resquest.data)
        if table_serializer.is_valid():
            object=Table.objects.get(id)
            table_serializer.update(object,table_serializer.validated_data)
        else:
            return Response({"success": False, "message": table_serializer.error_messages})


    def delete(self, request):

        table =Table.objects.get(pk=id).delete()
        return Response({'success': True, 'message': "Xóa thành công"})
