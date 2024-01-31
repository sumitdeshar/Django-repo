from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.serializers import UserRegistrationSerializer
from django.contrib.auth.models import User


class RegisterView(APIView):
    def post(self, request):
        data = request.data  # Use request.data to access JSON data

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        password2 = data.get("password2")

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({"message": "Email Already Used"}, status=status.HTTP_400_BAD_REQUEST)
            elif User.objects.filter(username=username).exists():
                return Response({"message": "Username Already Used"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user_data = {"username": username, "email": email, "password": password}
                serializer = UserRegistrationSerializer(data=user_data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Password did not match"}, status=status.HTTP_400_BAD_REQUEST)
