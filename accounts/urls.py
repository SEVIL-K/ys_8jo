from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.CustomTokenObtainPairView.as_view(), name = "login"),
]