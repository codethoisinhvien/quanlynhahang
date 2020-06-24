from httplib2 import Response
from rest_framework.views import APIView, Response

from src.serializers.food_group_serializer import FoodGroupSerializer, FoodGroupUpdateSerializer, FoodGroup


class FoodGroupApi(APIView):

    def post(self, request):
        food_group = FoodGroupSerializer(data=request.data)
        if food_group.is_valid():
            food_group.save()
            return Response({'success': True, 'data': food_group.data})
        else:
            return Response({'success': False, 'message': food_group.error_messages})

    def put(self, request, id=None):
        food_group = FoodGroupUpdateSerializer(data=request.data)
        if food_group.is_valid():
            object = FoodGroup.objects.get(pk=id)
            food_group.update(object, food_group.validated_data)
            return Response({'success': True, "data": food_group.instance})

    def get(self, requet):
        food_group = FoodGroup.objects.all()
        food_group_serializer = FoodGroupSerializer(food_group, many=True)
        return Response({'success': True, 'data': food_group_serializer.data})

    def delete(self, request, id=None):
        food_group = FoodGroup.objects.get(pk=id).delete()
        return Response({'success': True, 'message': "Xóa thành công"})
