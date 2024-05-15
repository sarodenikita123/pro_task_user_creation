from django.urls import path
from .views import *


urlpatterns = [
    path('otp/', OtpAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('deactivate/', Deactivate.as_view())
]
