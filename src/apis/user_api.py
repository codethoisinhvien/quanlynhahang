from rest_framework.views import APIView, Response

from src.models import User
from src.serializers.user_selializer import UserSerializer


class UsersApi(APIView):
    def get(self, request):
        user = User.objects.all()
        user_Serializer = UserSerializer(user, many=True)
        return Response({"success": True, "data": user_Serializer.data})

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'success': True, 'data': user_serializer.data})
        else:
            return Response({'success': False, 'message': user_serializer.errors})


class UserApi(APIView):

    def put(self, request, id=None):
        user = User.objects.get(pk=id)
        user_serializer = UserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'success': True, 'message': "Thành công "})
        return Response({'success': False, 'message': user_serializer.error_messages})

    def delete(self, request, id=None):
        try:
            User.objects.get(pk=id).delete()
            return Response({'success': True, 'message': "Thành công "})
        except:
            return Response({'success': False, 'message': "Thất bại"})
