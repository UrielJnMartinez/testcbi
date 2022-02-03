from django.shortcuts import render

# Create your views here.
from .models import PermisionsAsigned, Permisions, UserCBI
from .serializer import UserSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListAPIview(APIView):

    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        user = UserCBI.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIview(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return UserCBI.objects.get(pk=pk)
        except UserCBI.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCustomNumberAPIview(APIView):

    """
    List all users when phone number is different to 951 lada.
    """
    def get(self, request, format=None):
        user = UserCBI.objects.filter(status=True).exclude(phone_number__icontains = 951)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)