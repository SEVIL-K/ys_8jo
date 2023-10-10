from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import APIView, permission_classes
from rest_framework import status,permissions
from rest_framework.response import Response
from accounts.serializer import UserSerializer, CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        
)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class  token_test(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response("get요청")
    
@permission_classes((permissions.AllowAny,))   
class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message ": "가입완료"})
        else:
            return Response({"massage" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)