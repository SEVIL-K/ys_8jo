from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.CustomTokenObtainPairView.as_view(), name = "login"),
    path('signup/', views.SignUp.as_view(), name = "signup"),
]