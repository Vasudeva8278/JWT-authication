from django.urls import path
from .views import Register, LoginView, UserAPIView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('getuser/',UserAPIView.as_view())
]
