from rest_framework.views import APIView, Response

from drf_yasg.utils import swagger_auto_schema
from src.serializers.employee_serializer import EmployeeSerializer                   
from src.models import Emloyee

class EmployeeApi(APIView): 
    
    def post(self, resquest):  
        employee =  EmployeeSerializer(data=resquest.data)
        if employee.is_valid():
            employee.save()
            return Response({'success': True, 'data': employee.data})
        else: 
            return Response({'success': False, 'message': employee.error_messages})

    def put(self, resquest):
        employee = EmployeeSerializer(data=resquest.data)
        if employee.is_valid():
            e = Emloyee.objects.get(pk=id)
            employee.update(e,employee.validated_data)
            return Response({'success': True, 'data': employee.data})
        else: 
            return Response({'success': False, 'message': employee.error_messages})
    def delete(self, resquest):
        employee = Emloyee.objects.get(pk=id).delete()
        return Response({'success': True, 'message': "Xóa thành công"})
    def get(self, resquest):
        employee = Emloyee.objects.all()
        employee_serializer = EmployeeSerializer(employee,many=True)
        return Response({'success': True, "data": employee_serializer.data})