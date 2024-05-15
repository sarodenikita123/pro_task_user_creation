from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, User
from .models import Otp
from uuid import uuid4
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class OtpAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = str(uuid4())
        Otp.objects.create(email=email, otp=otp)
        return Response(data={"msg": "done"})


class UserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            otp = request.data.get('otp')
            print(otp)
            otp_obj = get_object_or_404(Otp, email=username, otp=otp)
            if otp_obj:
                serializer.save()
                return Response(data={"msg": 'save!!!'})
        return Response(data={'msg': 'done!!'})


class Deactivate(APIView):
    def post(self, request):
        username = request.data.get('username')
        if User:
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            return Response(data={"msg": 'user deactivated.'}, status=200)
        return Response(data={"error": "user not found"}, status=400)

