from django.shortcuts import render
from rest_framework import viewsets, response

from course.models import Payments
from users.models import User
from users.serializer import UserSerializer, CreateUserSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request):
        obj = User.objects.create(**request.data)
        serializer = CreateUserSerializer(obj)
        return response.Response(serializer.data)

    def partial_update(self, request, pk):
        obj = User.objects.get(pk=pk)
        for i, j in request.data.items():
            setattr(obj, i, j)
        obj.save()
        serializer = UserSerializer(obj)
        return response.Response(serializer.data)
