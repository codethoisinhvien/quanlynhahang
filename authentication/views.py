from rest_framework.views import APIView, Response

from commons.services.JWT_provider import JWTProvider
from .models import User

class AuthenticationAPI(APIView):
    def post(self, request):
        print(request.data['username'], request.data['password'])
        jwt = JWTProvider()
        queryset = User.objects.get(username=request.data['username'])
        print(queryset.username)
        return Response({"success": True, "access_tọken": jwt.generateToken(123456)})
