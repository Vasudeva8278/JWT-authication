from django.urls import path
from .views import Home,Reg


urlpatterns = [
    path('', Home.as_view()),
    path("reg",Reg.as_view())
]


