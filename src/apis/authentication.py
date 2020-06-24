from rest_framework.views import APIView, Response

from src.models import User
from src.serializers.user_selializer import UserSerializer


class AuthenticationApi(APIView):

    def post(self, request):
        try:
            user = User.objects.get(username=request.data['username'])
            print(user)
            user_serializer = UserSerializer(user)
            if user.password == request.data['password']:
                return Response({'success': True, 'token': "", 'data': user_serializer.data})
            return Response({'success': False, 'message': "Tài khoản hoac mật khẩu khong đúng"})
        except:
            return Response({'success': False, 'message': "Tài khoản hoac mật khẩu không đúng"})
