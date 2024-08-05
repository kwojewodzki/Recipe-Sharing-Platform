from django.shortcuts import render
from rest_framework import views, permissions
from rest_framework.response import Response
# Create your views here.


class LoginView(views.APIView):
    
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Login here'})
