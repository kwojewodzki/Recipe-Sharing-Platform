from django.shortcuts import render
from django.contrib.auth.models import User
from my_auth.serializers import RegisterSerializer

from rest_framework import generics, permissions

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)