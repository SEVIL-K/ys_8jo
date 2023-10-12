from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('', views.CustomTokenObtainPairView.as_view(), name = "login"),
    path("mocks/", views.Token_Test.as_view(), name="login_test"),
    
]