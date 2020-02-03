from rest_framework.views import APIView, Response

from src.models import TableGroup
from src.serializers.table_group_serializer import TableGroupSerializer, TableGroupUpdateSerializer


class TableGroupApi(APIView):
    def post(self, request):
        table_group_serializer = TableGroupSerializer(data=request.data)
        if table_group_serializer.is_valid():
            table_group_serializer.save()
            return Response({"success": True, 'table_group': table_group_serializer.data})
        else:
            return Response({"success": False, 'message': table_group_serializer.errors})

    def get(self, request):
        table_group = TableGroup.objects.all()
        table_group_serializer = TableGroupSerializer(table_group, many=True)
        return Response({"success": True, 'table_groups': table_group_serializer.data})

    def put(self, request, id=None):
        table_group_serializer = TableGroupUpdateSerializer(data=request.data)
        if table_group_serializer.is_valid():
            object = TableGroup.objects.get(pk=id)
            table_group_serializer.update(object,table_group_serializer.validated_data)
            return Response({"success": True, 'table_group': table_group_serializer.data})
        else:
            return Response({"success": False, 'message': table_group_serializer.errors})

    def delete(self, request, id=None):
        table_group = TableGroup.objects.get(pk=id).delete()
        return Response({"success": True, 'message': "Xóa thành công"})
