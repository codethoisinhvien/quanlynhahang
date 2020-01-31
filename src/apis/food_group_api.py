from httplib2 import Response
from rest_framework.views import APIView,Response

class FoodGroupApi(APIView):

  def post(self,request):
    name= request.data['name']
    return Response({'success':True,'name':name})

