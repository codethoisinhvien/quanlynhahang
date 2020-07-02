from rest_framework.views import APIView, Response
from django.db.models import Sum,Count
from src.models import Customer,Bill
# from django.db.models.expressions import D
from src.serializers.office_serializer import OfficeSerializer
from src.serializers.statistic_serializer import BillStatisticSerializer


class StatisticApi(APIView):
    def get(self, request):

        money = Bill.objects.all().\
            extra({'date': "date(created_at)"}). \
            values('date'). \
            annotate(total_money=Sum('total_money'),total_bill=Count('id'))
        a= BillStatisticSerializer(money,many=True)
        return Response({"success": True,
                         "data":{
                             "statistic":a.data


                                                  }})
