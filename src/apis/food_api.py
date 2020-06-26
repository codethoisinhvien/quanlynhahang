from django.db.models import Q
from django.db.models import Sum
from rest_framework.views import APIView, Response

from src.models import Food, BillDetail
from src.serializers.food_serializer import FoodSerializer, FoodUpdateSerializer, BestFoodSerializer


class FoodApi(APIView):

    def post(self, request):
        food_serializer = FoodSerializer(data=request.data)
        if food_serializer.is_valid():
            food_serializer.save()
            return Response({'success': True, 'data': food_serializer.data})
        else:
            return Response({'success': False, 'message': food_serializer.error_messages})

    def put(self, request, id=None):
        food_group = FoodUpdateSerializer(data=request.data)
        if food_group.is_valid():
            object = Food.objects.get(pk=id)
            food_group.update(object, food_group.validated_data)
            return Response({'success': True, "data": food_group.data})

    def get(self, request):
        condition = Q()
        food_group = request.GET.get('group')

        if food_group is not None and food_group.isnumeric():
            condition = condition & Q(food_group=food_group)

        food = Food.objects.filter(condition)
        food_serializer = FoodSerializer(food, many=True)
        return Response({'success': True, 'data': food_serializer.data})

    def delete(self, request, id=None):

        food_group = Food.objects.get(pk=id).delete()
        return Response({'success': True, 'message': "Xóa thành công"})


class BestFood(APIView):
    def get(self, request):
        best_food = BillDetail.objects.values('food__name','food') \
            .order_by('food').annotate(count=Sum('amount'),count_complete=Sum('amount_complete')).filter()
        best_food_serializer = BestFoodSerializer(best_food, many=True)
        return Response({'success': True,
                         'best_food': best_food_serializer.data
                         })
