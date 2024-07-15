from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # Import AllowAny permission class
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
class Register(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access for testing

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = user.object.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed("user not Found")
        
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect ceridential')
        return Response(user)