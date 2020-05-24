
from rest_framework.views import APIView, Response

from src.models import Office
from src.serializers.office_serializer import OfficeSerializer


class OfficeApi(APIView):
    def get(self, request):
        offices = Office.objects.all()
        officeSerializer = OfficeSerializer(offices, many=True)
        return Response({"success": True, "data": officeSerializer.data})
