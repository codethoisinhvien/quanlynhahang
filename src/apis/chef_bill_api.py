
from rest_framework.views import APIView, Response
from src.models import ChefBill
class ChefBillApi(APIView):
    def delete(self, request, id=None):
        chef_bill =ChefBill.objects.get(pk=id).delete()
        return Response({'success': True, 'message': "Xóa thành công"})
