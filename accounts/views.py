from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from accounts.serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class  token_test(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response("get요청")