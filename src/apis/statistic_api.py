from rest_framework.views import APIView, Response
from django.db.models import Sum
from src.models import Customer,Bill
# from django.db.models.expressions import D
from src.serializers.office_serializer import OfficeSerializer
from src.serializers.statistic_serializer import BillStatisticSerializer


class StatisticApi(APIView):
    def get(self, request):

        money = Bill.objects.all().\
            extra({'date': "date(created_at)"}). \
            values('date'). \
            annotate(total=Sum('total_money'))
        a= BillStatisticSerializer(money,many=True)
        return Response({"success": True,
                         "data":{
                             "total_money":a.data


                                                  }})
