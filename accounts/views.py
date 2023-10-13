
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from accounts.serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from rest_framework.decorators import APIView, permission_classes
from accounts.serializer import UserSerializer

@permission_classes((permissions.AllowAny,))   #인증되지않은 사용자도 api에 접근허용
class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message ": "가입완료"})
        else:
            return Response({"massage" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class  Token_Test(APIView):
    permission_classes=[permissions.IsAuthenticated] #인증된사용자만 뷰에 접근(api)
    def get(self, request):
        print(request.user)
        return Response("get요청")
    
    
