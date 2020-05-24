from rest_framework.views import APIView, Response

from src.models import User
from src.serializers.user_selializer import UserSerializer


class UserApi(APIView):
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
