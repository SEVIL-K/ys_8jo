from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    #그렇기에 클래스 메소드는 첫번째 매개변수로 클래스 자체를 받게 된다. cls
    @classmethod
    def get_token(cls,user):#오버라이드 내장된 get_token(user)
        token = super().get_token(user)
        #오버라이드 get_token(user)
        token['email'] = user.email
        return token
    

    def create(self, validated_data):
        user = super().create(validated_data)
        print(validated_data)
        password = user.password
        user.set_password(password)
        print(user.password)

        return super().create(validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        