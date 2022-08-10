from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *
from .models import CustomUser

class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, **validated_data):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Signed up successfully!')


class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListUsersSerializer